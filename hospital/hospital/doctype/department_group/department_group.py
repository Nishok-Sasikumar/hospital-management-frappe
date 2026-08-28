
# class DepartmentGroup(NestedSet):
# 	pass
# Copyright (c) 2026, Nishok and contributors
# For license information, please see license.txt
import frappe
from frappe import _
from frappe.query_builder import functions
from frappe.utils import cint
from frappe.utils.nestedset import NestedSet


class DepartmentGroup(NestedSet):
	nsm_parent_field = "parent_department_group"

	def validate(self):
		if not self.department_group_name:
			frappe.throw(_("Department Group Name is required"))

		self.validate_duplicate_name()

	def validate_duplicate_name(self):
		"""Prevent two sibling nodes under the same parent from sharing a name."""
		existing = frappe.db.exists(
			"Department Group",
			{
				"department_group_name": self.department_group_name,
				"parent_department_group": self.parent_department_group,
				"name": ["!=", self.name],
			},
		)
		if existing:
			frappe.throw(
				_("A Department Group named {0} already exists under the same parent").format(
					frappe.bold(self.department_group_name)
				)
			)


def _to_bool(value) -> bool:
	if isinstance(value, bool):
		return value
	return bool(cint(value)) if str(value).isdigit() else str(value).lower() == "true"

@frappe.whitelist()
def get_children(doctype: str, parent: str | None = None, is_root=False, **filters):
	"""Returns children of a Department Group node, with child counts for badges."""
	parent_field = "parent_department_group"
	is_root = _to_bool(is_root)

	if is_root or parent in (None, "", "Department Group", doctype):
		parent = ""

	table = frappe.qb.DocType("Department Group")

	query = (
		frappe.qb.from_(table)
		.select(
			table.name.as_("value"),
			table.department_group_name.as_("title"),
			table.is_group.as_("expandable"),
			table.description,
		)
		.where(functions.IfNull(table[parent_field], "").eq(parent))
		.where(table.docstatus < 2)
		.orderby(table.name)
	)

	nodes = query.run(as_dict=True)

	# attach a child count to every group node, so the JS can show a badge
	group_names = [n.value for n in nodes if n.expandable]
	if group_names:
		count_table = frappe.qb.DocType("Department Group")
		count_query = (
			frappe.qb.from_(count_table)
			.select(
				count_table[parent_field].as_("parent_name"),
				functions.Count(count_table.name).as_("count"),
			)
			.where(count_table[parent_field].isin(group_names))
			.where(count_table.docstatus < 2)
			.groupby(count_table[parent_field])
		)
		counts = count_query.run(as_dict=True)
		count_map = {c.parent_name: c.count for c in counts}

		for node in nodes:
			if node.expandable:
				node["child_count"] = count_map.get(node.value, 0)

	return nodes
@frappe.whitelist()
def add_node():
	"""Called when a user adds a new node from the tree's Add dialog."""
	args = frappe.form_dict
	args.pop("cmd", None)

	department_group_name = args.get("department_group_name")
	if not department_group_name:
		frappe.throw(_("Department Group Name is required"))

	doc = frappe.new_doc("Department Group")
	doc.department_group_name = department_group_name
	doc.is_group = cint(args.get("is_group"))
	doc.description = args.get("description")

	parent = args.get("parent")
	is_root = _to_bool(args.get("is_root"))

	if parent and not is_root and parent != "Department Group":
		doc.parent_department_group = parent

	doc.insert()
	frappe.msgprint(_("Department Group {0} created").format(doc.name), alert=True)

	return doc.name