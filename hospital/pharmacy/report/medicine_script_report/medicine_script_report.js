// Copyright (c) 2026, Nishok and contributors
// For license information, please see license.txt

frappe.query_reports["Medicine Query Report"] = {
    "filters": [
        {
            "fieldname": "medicine_name",
            "label": __("Medicine Name"),
            "fieldtype": "Data",
            "placeholder": "Search medicine..."
        }
    ]
};