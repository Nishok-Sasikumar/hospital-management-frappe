# Copyright (c) 2026, Nishok and contributors
# For license information, please see license.txt
import frappe
import os
from frappe.model.document import Document


class Doctor(Document):

    @property
    def doctor_summary(self):
        exp_text = f"{self.experience} yrs experience" if self.experience else "experience not set"
        return f"Dr. {self.doctor_name} ({self.department or 'No Dept'}) - {exp_text}"

    def custom_validation(self):
        if self.available and not self.consultation_fee:
            frappe.throw("Please set a Consultation Fee before marking this doctor as Available.")

    def write_file(self):
        folder = frappe.get_site_path('private', 'files', 'doctor_notes')
        os.makedirs(folder, exist_ok=True)
        self._file_path = os.path.join(folder, f"{self.name}.txt")
        with open(self._file_path, 'w') as f:
            f.write(f"Welcome, Dr. {self.doctor_name}!")
        print(f"[write_file] File created at {self._file_path}")

    def delete_file(self):
        if hasattr(self, '_file_path') and os.path.exists(self._file_path):
            os.remove(self._file_path)
            print(f"[delete_file] File removed: {self._file_path}")

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
        self.write_file()
        frappe.db.after_rollback.add(self.delete_file)
        frappe.db.after_commit.add(lambda: print(f"[after_commit] {self.name} is now permanently saved."))


        frappe.publish_realtime('new_doctor_registered', {
            'name': self.name,
            'doctor_name': self.doctor_name,
            'department': self.department
        })
        # frappe.publish_progress(25,title="Doctor Registration", description=f"Doctor {self.doctor_name} registered successfully.")

    def on_update(self):
        frappe.logger().info(f"Doctor {self.name} updated by {frappe.session.user}")
        frappe.publish_realtime('doctor_updated', {
            'name': self.name,
            'doctor_name': self.doctor_name,
            'consultation_fee': self.consultation_fee
        })

    def on_trash(self):
        if self.available == 1:
            frappe.throw("Cannot delete an available doctor. Mark the doctor as unavailable first.")

    def send_reminder_email(self, message="Reminder"):
        if not self.email:
            frappe.log_error(f"No email set for Doctor {self.name}")
            return
        frappe.sendmail(
            recipients=[self.email],
            subject="Reminder for Dr. " + self.doctor_name,
            message=message
        )
        frappe.logger().info(f"Reminder email sent to {self.email} for {self.name}")

    # frm.call use this method to get upcoming schedules for the doctor(for this it should require a doctoe schedule)
    @frappe.whitelist()
    def get_upcoming_schedule(self):
        schedules = frappe.get_all(
            'Doctor Schedule',
            filters={
                'doctor': self.name,
                'schedule_date': ['>=', frappe.utils.today()],
                'docstatus': 1
            },
            fields=['name', 'schedule_date', 'start_time', 'end_time'],
            order_by='schedule_date asc'
        )
        return schedules