# Copyright (c) 2026, Nishok and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
class Doctor(Document):

    @property
    def doctor_summary(self):
        exp_text = f"{self.experience} yrs experience" if self.experience else "experience not set"
        return f"Dr. {self.doctor_name} ({self.department or 'No Dept'}) - {exp_text}"

    def custom_validation(self):
        if self.available and not self.consultation_fee:
            frappe.throw("Please set a Consultation Fee before marking this doctor as Available.")

    def before_insert(self):
        if self.doctor_name:
            self.doctor_name = self.doctor_name.title()
        self.available = 1
        if not self.consultation_fee:
            self.consultation_fee = 500
        if not self.biography:
            self.biography = (f"Dr. {self.doctor_name} works in the {self.department} department.")

    def validate(self):
        if self.experience is not None and self.experience < 0:
            frappe.throw("Experience cannot be negative")
        if self.consultation_fee is not None and self.consultation_fee < 0:
            frappe.throw("Consultation Fee cannot be negative")
        if self.email and "@" not in self.email:
            frappe.throw("Enter a valid email address")
        self.custom_validation()

    def printhello(self):
        return 10
    def before_save(self):
        if self.experience and self.experience >= 10:
            current_fee = self.consultation_fee or 0
            self.consultation_fee = max(current_fee, 1000)
        if self.experience:
            self.biography = (f"Dr. {self.doctor_name} has {self.experience} years of experience in {self.department}.")

    def after_insert(self):
        frappe.msgprint(f"Doctor {self.doctor_name} has been registered successfully.")

    def on_update(self):
        frappe.logger().info(f"Doctor {self.name} updated by {frappe.session.user}")

    def on_trash(self):
        if self.available == 1:
            frappe.throw("Cannot delete an available doctor. Mark the doctor as unavailable first.")