import frappe
from frappe.model.document import Document


class Doctor(Document):

    @property
    def doctor_summary(self):
        # stitches a few fields into one readable sentence
        exp_text = f"{self.experience} yrs experience" if self.experience else "experience not set"
        return f"Dr. {self.doctor_name} ({self.department or 'No Dept'}) - {exp_text}"

    def custom_validation(self):
        # if doctor is marked available, they must have a consultation fee set
        if self.available and not self.consultation_fee:
            frappe.throw("Please set a Consultation Fee before marking this doctor as Available.")

    def validate(self):
        self.custom_validation()    # run our extra check

    def on_trash(self):
        if self.available == 1:
            frappe.throw("Cannot delete an available doctor. Mark the doctor as unavailable first.")