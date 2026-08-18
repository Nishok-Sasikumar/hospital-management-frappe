# hospital/hospital/api.py
import frappe
from frappe import _, qb


@frappe.whitelist()
def get_doctors_with_owner_info(limit: int = 5):

    # QUERY BUILDER — join Doctor with User (via the owner field)
    Doctor = qb.DocType("Doctor")
    User = qb.DocType("User")

    query = (
        qb.from_(Doctor)
        .join(User)
        .on(Doctor.owner == User.name)
        .select(
            Doctor.name,
            Doctor.doctor_name,
            Doctor.medical_license,
            Doctor.doctor_photo,
            Doctor.creation,
            Doctor.modified,
            User.full_name.as_("owner_full_name"),
            User.email.as_("owner_email"),
        )
        .limit(limit)
    )

    results = query.run(as_dict=True)

    if not results:
        return {"message": "No Doctor records found", "data": []}

    # DOCUMENT API — fetch one record, update a field, save it
    first_doctor_name = results[0]["name"]
    doc = frappe.get_doc("Doctor", first_doctor_name)
    doc.biography = (doc.biography or "") + " [Synced via API]"
    doc.save(ignore_permissions=True)

    # DATABASE API — bulk update across ALL fetched records, bypassing validations
    all_names = [row["name"] for row in results]
    frappe.db.set_value(
        "Doctor",
        {"name": ["in", all_names]},
        "last_synced_on",
        frappe.utils.now(),
    )

    frappe.db.commit()

    return {
        "message": f"Processed {len(results)} doctor(s)",
        "updated_via_doc_api": first_doctor_name,
        "bulk_updated_names": all_names,
        "data": results,
    }


@frappe.whitelist()
def download_medical_license(doctor_name):
    """
    Downloads the medical license file for a specific doctor.
    Example of a file-download response using Frappe's response system.
    Requires login (allow_guest removed intentionally — this is sensitive data).
    """
    if not frappe.db.exists('Doctor', doctor_name):
        frappe.throw(_("Doctor not found"))

    doctor = frappe.get_doc('Doctor', doctor_name)

    if not doctor.medical_license:
        frappe.throw(_("No medical license file attached to this doctor"))

    try:
        file_doc = frappe.get_doc('File', doctor.medical_license)
    except Exception:
        frappe.throw(_("License file record not found in database"))

    if not file_doc.file_name:
        frappe.throw(_("File content missing"))

    frappe.response['type'] = 'download'
    frappe.response['filename'] = f"{doctor.doctor_name or doctor_name}_medical_license.pdf"
    frappe.response['filecontent'] = file_doc.get_content()
    frappe.response['display_content_as'] = 'attachment'

    return None


@frappe.whitelist()
def get_recent_todos_with_owner_emails():
    """
    Demonstrates frappe.get_list() (permission-aware), frappe.db.get_value()
    (optimized single-value fetch), and frappe.utils.now() (context-aware timestamp).
    """
    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit_page_length=5
    )

    for todo in todos:
        todo["owner_email"] = frappe.db.get_value("User", todo["owner"], "email")
        todo["description"] = frappe.utils.strip_html(todo["description"])

    timestamp = frappe.utils.now()

    return {
        "timestamp": timestamp,
        "records": todos
    }