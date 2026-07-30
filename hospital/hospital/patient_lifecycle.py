import frappe
from frappe.utils import getdate, nowdate

def custom_before_naming(doc, method):
    """
    1. before_naming: Prepares data right before naming runs.
    """
    if doc.patient_name:
        doc.patient_name = doc.patient_name.strip()


def custom_autoname(doc, method):
    """
    2. autoname: Generates and assigns the primary ID (doc.name).
       Note: When using hooks for autoname, you assign the name to doc.name directly.
    """
    if doc.phone:
        last_digits = doc.phone[-4:]
        doc.name = f"PAT-MED-{last_digits}"
    else:
        doc.name = frappe.generate_hash("Patient", 6)


def set_default_patient_data(doc, method):
    """
    3. before_insert: Fires right after naming is done.
    """
    if doc.patient_name:
        doc.patient_name = doc.patient_name.title()


def validate_patient_info(doc, method):
    """
    4. validate: Core field validation stage.
    """
    if doc.date_of_birth and getdate(doc.date_of_birth) > getdate(nowdate()):
        frappe.throw("Date of Birth cannot be in the future!")
        
    if doc.phone and len(str(doc.phone)) < 10:
        frappe.throw("Phone number must contain at least 10 digits.")


def final_patient_cleanup(doc, method):
    """
    5. before_save: Final modifications right before database write.
    """
    doc.custom_registration_status = "Verified"


def log_new_patient_creation(doc, method):
    """
    6. after_insert: Post-database-save actions.
    """
    frappe.msgprint(f"Welcome record created successfully for Patient: {doc.patient_name} (ID: {doc.name})")