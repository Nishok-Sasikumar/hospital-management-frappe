import frappe

def get_extra_site_info(site_info):
    return {
        "total_patients": frappe.db.count("Patient"),
        "total_appointments": frappe.db.count("Patient Apointment"),
    }