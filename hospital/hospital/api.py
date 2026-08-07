import frappe
from frappe import _
from frappe.utils import validate_email

@frappe.whitelist(allow_guest=True)
def create_signup_request(email, full_name, phone_number=None, department="General Medicine"):
    if not email or not validate_email(email):
        frappe.throw(_("Please provide a valid email address."))

    # Check for existing pending/approved requests
    existing = frappe.db.exists("Hospital Signup Request", {"email": email, "status": ["in", ["Pending", "Approved"]]})
    if existing:
        frappe.throw(_("A registration request for this email already exists or is processed."))

    # Insert entry into the Hospital Signup Request DocType
    doc = frappe.get_doc({
        "doctype": "Hospital Signup Request",
        "email": email,
        "full_name": full_name,
        "phone_number": phone_number,
        "department": department,
        "status": "Pending"
    })
    doc.insert(ignore_permissions=True)

    return {"status": "success"}