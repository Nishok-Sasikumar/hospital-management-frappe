# import frappe


# def cus_1_has_permission(doc, user=None, permission_type=None):
#     if not user:
#         user = frappe.session.user

#     # Administrator / System Manager always has access
#     if user == "Administrator" or "System Manager" in frappe.get_roles(user):
#         return True

#     # Only the owner can read/write/delete/open this document
#     if doc.owner == user:
#         return True

#     # Explicitly deny everyone else — do NOT return None here,
#     # otherwise it falls back to default permissions and lets them through
#     return False


# def cus_1_query_conditions(user):
#     if not user:
#         user = frappe.session.user

#     if user == "Administrator" or "System Manager" in frappe.get_roles(user):
#         return ""

#     # Restricts list view / report view to only docs owned by the user
#     return f"(`tabCus_1`.`owner` = {frappe.db.escape(user)})"