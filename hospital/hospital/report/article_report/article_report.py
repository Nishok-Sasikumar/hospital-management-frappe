import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": _("Title"),
            "fieldname": "title",
            "fieldtype": "Data",
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
        },
        {
            "label": _("Amount"),
            "fieldname": "amount",
            "fieldtype": "Currency",
        },
        {
            "label": _("Posting Date"),
            "fieldname": "posting_date",
            "fieldtype": "Date",
        },
    ]

    data = [
        ["News", "Published", 1500, "2026-09-01"],
        ["Technology Update", "Published", 2500, "2026-09-05"],
        ["Company News", "Draft", 1000, "2026-09-10"],
    ]

    return columns, data
	