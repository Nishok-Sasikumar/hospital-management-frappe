import frappe
@frappe.whitelist()
def create_patient():
    patient = frappe.get_doc({
        "doctype": "Patient",
        "patient_name": "Rahul",
        "date_of_birth": "2026-07-30",
        "phone": "+919876543210",
        "blood_group": "A+"
    })

    # Save the document
    patient.insert()

    return {
        "status": "success",
        "message": "Patient created successfully",
        "patient_id": patient.name,
        "patient_name": patient.patient_name,
        "phone": patient.phone,
        "blood_group": patient.blood_group
    }


@frappe.whitelist()
def get_patient(patient_id):
    """
    Fetch a Patient document using the Document API.
    """

    patient = frappe.get_doc("Patient", patient_id)

    return {
        "patient_id": patient.name,
        "patient_name": patient.patient_name,
        "phone": patient.phone,
        "blood_group": patient.blood_group,
        "date_of_birth": patient.date_of_birth
    }


@frappe.whitelist()
def update_patient(patient_id):
    """
    Update a Patient document using the Document API.
    """

    patient = frappe.get_doc("Patient", patient_id)

    patient.phone = "+919999999999"

    patient.save()

    return {
        "status": "success",
        "message": "Patient updated successfully",
        "patient_id": patient.name,
        "new_phone": patient.phone
    }


