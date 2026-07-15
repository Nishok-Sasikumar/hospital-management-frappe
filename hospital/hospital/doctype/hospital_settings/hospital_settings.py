# Copyright (c) 2026, Nishok and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address

# class HospitalSettings(Document):
#  	pass
class HospitalSettings(Document):
	def before_save(self):
		if self.hospital_name:
			self.hospital_name = self.hospital_name.title()
		else:
			frappe.throw("Hospital Name is required.")
		if self.phone:
			if len(self.phone) != 14:
				frappe.throw("Phone Number must be a 14-digit number.")