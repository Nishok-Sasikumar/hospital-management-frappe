import frappe

def execute(filters=None):
    # Step 1: Define Columns
    columns = [
        {"label": "ID", "fieldname": "name", "fieldtype": "Link", "options": "Medicine", "width": 120},
        {"label": "Owner", "fieldname": "owner", "fieldtype": "Data", "width": 150},
    ]

    # Step 2: Fetch Data safely
    data = frappe.db.get_all(
        "Medicine",
        fields=["name", "owner"]
    )

    # Step 3: Return result
    return columns, data