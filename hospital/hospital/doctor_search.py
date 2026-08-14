# hospital/hospital/doctor_search.py
import frappe
from frappe.search.full_text_search import FullTextSearch
from whoosh.fields import Schema, ID, TEXT


class DoctorSearch(FullTextSearch):

    def get_schema(self):
        return Schema(name=ID(stored=True), content=TEXT(stored=True))

    def get_id(self):
        return "name"

    def get_items_to_index(self):
        docs = []
        for doctor_name in frappe.get_all('Doctor', pluck='name'):
            docs.append(self.get_document_to_index(doctor_name))
        return docs

    def get_document_to_index(self, name):
        doctor = frappe.get_doc('Doctor', name)
        return frappe._dict(name=doctor.name, content=doctor.biography or "")

    def parse_result(self, result):
        return result["name"]