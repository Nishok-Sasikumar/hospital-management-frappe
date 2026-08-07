import frappe
from frappe import _
import pyotp
import time


# ---------------------------------------------------------
# CONFIG: Store these in site_config.json, NOT hardcoded here
# ---------------------------------------------------------
# bench --site your-site set-config twilio_account_sid "ACxxxxxxxx"
# bench --site your-site set-config twilio_auth_token "xxxxxxxx"
# bench --site your-site set-config twilio_sender_number "+1415XXXXXXX"

def get_twilio_client():
    from twilio.rest import Client

    account_sid = frappe.conf.get("twilio_account_sid")
    auth_token = frappe.conf.get("twilio_auth_token")

    if not account_sid or not auth_token:
        frappe.throw(_("Twilio credentials not configured in site_config.json"))

    return Client(account_sid, auth_token)


def _normalize_numbers(receiver_list):
    """Ensure we always work with a list of numbers"""
    if isinstance(receiver_list, str):
        return [receiver_list]
    return receiver_list


# ---------------------------------------------------------
# 1. General SMS sending (notifications, bulk SMS, alerts)
# ---------------------------------------------------------
def send_sms(receiver_list, msg, sender=None, success_msg=True):
    """
    Override default Frappe SMS sending logic.

    Args:
        receiver_list: list of mobile numbers, or single number as string
        msg: SMS message content
        sender: Sender ID/number (optional, falls back to configured default)
        success_msg: whether to show a success message in the UI
    """
    receiver_list = _normalize_numbers(receiver_list)

    if not receiver_list:
        frappe.log_error("No recipients provided for SMS", "SMS Send Error")
        return False

    from_number = sender or frappe.conf.get("twilio_sender_number")
    client = get_twilio_client()

    failed_numbers = []

    for number in receiver_list:
        try:
            # Basic number sanity check — adjust regex/logic to your locale
            number = number.strip()
            if not number:
                continue

            message = client.messages.create(
                body=msg,
                from_=from_number,
                to=number
            )

            frappe.logger().info(f"SMS sent to {number}, SID: {message.sid}")

        except Exception as e:
            failed_numbers.append(number)
            frappe.log_error(
                message=f"Failed to send SMS to {number}: {str(e)}",
                title="SMS Send Failure"
            )

    if failed_numbers:
        frappe.msgprint(
            _("Failed to send SMS to: {0}").format(", ".join(failed_numbers)),
            indicator="red"
        )
        # Don't throw if some succeeded — only throw if ALL failed
        if len(failed_numbers) == len(receiver_list):
            frappe.throw(_("Failed to send SMS to all recipients"))
        return False

    if success_msg:
        frappe.msgprint(_("SMS sent successfully"), indicator="green")

    return True


# ---------------------------------------------------------
# 2. OTP / Two-Factor Authentication SMS
# ---------------------------------------------------------
def send_token_via_sms(otpsecret, token=None, phone_no=None):
    """
    Generate an OTP using HOTP and send it via SMS for 2FA / login flows.

    Args:
        otpsecret: base32 secret used to generate the HOTP
        token: counter value used for HOTP generation (Frappe passes this)
        phone_no: destination mobile number
    """
    if not phone_no:
        frappe.log_error("No phone number provided for OTP", "OTP Error")
        return False

    try:
        token_int = int(token) if token else int(time.time())

        hotp = pyotp.HOTP(otpsecret)
        otp_code = hotp.at(token_int)

        message_body = _(
            "Your Hospital login OTP is {0}. Valid for 5 minutes. Do not share this code."
        ).format(otp_code)

        success = send_sms(
            receiver_list=[phone_no],
            msg=message_body,
            success_msg=False  # don't show generic "SMS sent" popup for OTPs
        )

        return success

    except Exception as e:
        frappe.log_error(
            message=f"Failed to send OTP to {phone_no}: {str(e)}",
            title="OTP Error"
        )
        return False