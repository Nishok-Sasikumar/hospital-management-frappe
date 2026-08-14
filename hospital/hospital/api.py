import frappe
from frappe import _

@frappe.whitelist()
def get_doctors_with_owner_info():
    doctors = frappe.get_all(
        'Doctor',
        fields=['name', 'doctor_name', 'medical_license', 'doctor_photo', 'owner', 'creation', 'modified'],
        filters={'docstatus': 1} 
    )
    
    result = []
    for doctor in doctors:
        user = None
        if doctor.owner:
            try:
                user = frappe.get_doc('User', doctor.owner)
            except Exception:
                user = None
        
        doctor_data = {
            'doctor_id': doctor.name,
            'doctor_name': doctor.doctor_name,
            'medical_license': doctor.medical_license,
            'doctor_photo': doctor.doctor_photo,
            'owner_email': user.email if user else None,
            'owner_full_name': user.full_name if user else None,
            'created_on': doctor.creation,
            'last_modified': doctor.modified,
            'last_synced_on': doctor.modified,
            'updated_via_doc_api': True,
            'bulk_updated_names': [doctor.name]
        }
        result.append(doctor_data)
    return {
        'data': result,
        'updated_via_doc_api': True,
        'bulk_updated_names': [d['doctor_id'] for d in result]
    }

@frappe.whitelist(allow_guest=True)
def download_medical_license(doctor_name):
    """
    Downloads the medical license file for a specific doctor.
    Example of file download response using Frappe's response system.
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