import frappe
def successful_login(login_manager):
    user = login_manager.user
    frappe.msgprint(f"User {user} logged in successfully")
    # Removed the last_login_ip line — not a real field