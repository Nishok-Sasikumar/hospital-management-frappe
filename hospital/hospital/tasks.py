# hospital/tasks.py
import frappe

def hourly_task():
    frappe.logger().info("Hourly task running")

def daily_task():
    frappe.logger().info("Daily task running")
    # e.g. mark past-due appointments as missed

def weekly_task():
    frappe.logger().info("Weekly task running")

def monthly_task():
    frappe.logger().info("Monthly task running")

def daily_long_task():
    frappe.logger().info("Long daily task running")
    # e.g. generate monthly patient reports, backups

def every_six_minutes_task():
    frappe.logger().info("Runs every 6 minutes")
# hospital/hospital/tasks.py
import frappe


def daily_maintenance():
    frappe.log_error(
        title="Daily Maintenance",
        message="Daily maintenance job executed successfully."
    )