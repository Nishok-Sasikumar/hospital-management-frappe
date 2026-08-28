// Copyright (c) 2026, Nishok and contributors
// // For license information, please see license.txt

frappe.treeview_settings["Department Group"] = {
	breadcrumb: "Hospital",
	title: __("Department Group Tree"),
	root_label: "All Department Groups",

	get_tree_nodes: "hospital.hospital.doctype.department_group.department_group.get_children",
	add_tree_node: "hospital.hospital.doctype.department_group.department_group.add_node",

	filters: [
		{
			fieldname: "search",
			fieldtype: "Data",
			label: __("Search"),
			render_on_toolbar: true,
			on_change: function () {
				let value = frappe.treeview_settings["Department Group"].filters[0].value;
				cur_tree.tree.$w.find(".tree-node").each(function () {
					let label = $(this).find(".tree-label").text().toLowerCase();
					let match = !value || label.includes((value || "").toLowerCase());
					$(this).toggle(match);
				});
			},
		},
	],

	fields: [
		{
			fieldtype: "Data",
			fieldname: "department_group_name",
			label: __("Department Group Name"),
			reqd: true,
		},
		{
			fieldtype: "Check",
			fieldname: "is_group",
			label: __("Is Group"),
			default: 0,
		},
		{
			fieldtype: "Small Text",
			fieldname: "description",
			label: __("Description"),
		},
		{
			fieldtype: "Small Text",
			fieldname: "new_description",
			label: __("New Description"),
		},
	],

	ignore_fields: ["description","is_group"],

	onload: function (treeview) {
		treeview.page.set_title(__("Department Groups"));
	},

	post_render: function (treeview) {
		treeview.page.set_indicator(__("Tree View"), "blue");

		// Quick link back to the standard list view
		treeview.page.add_menu_item(__("Switch to List View"), () => {
			frappe.set_route("List", "Department Group");
		});
	},

	onrender: function (node) {
		// Bold + folder-style label for group nodes
		if (node.expandable) {
			$(node.$tree_link).addClass("bold");
		}

		// Show a small count badge next to group nodes, once children are known
		if (node.expandable && node.data && node.data.child_count !== undefined) {
			$(node.$tree_link).append(
				`<span class="badge pull-right text-muted" style="margin-left: 6px;">${node.data.child_count}</span>`
			);
		}

		// Tooltip with description, if present
		if (node.data && node.data.description) {
			$(node.$tree_link).attr("title", node.data.description);
		}

		// Visually mark leaf (non-group) nodes differently
		if (!node.expandable) {
			$(node.$tree_link).css("opacity", "0.8");
		}
	},

	extend_toolbar: true,
	toolbar: [
		{
			label: __("Expand All"),
			condition: function () {
				return true;
			},
			click: function () {
				$(".tree-children").show();
				$(".tree-link .octicon-chevron-right, .tree-link svg[data-icon='chevron-right']").each(
					function () {
						$(this).closest(".tree-link").trigger("click");
					}
				);
			},
			btnClass: "hidden-xs",
		},
		{
			label: __("Collapse All"),
			condition: function () {
				return true;
			},
			click: function () {
				$(".tree-children").hide();
			},
			btnClass: "hidden-xs",
		},
	],

	menu_items: [
		{
			label: __("Refresh Tree"),
			action: function () {
				cur_tree && cur_tree.refresh();
				frappe.msgprint('refresshed...');
			},
		},
		{
			label: __("New Department Group"),
			action: function () {
				frappe.new_doc("Department Group");
			},
			condition: "frappe.boot.user.can_create.indexOf('Department Group') !== -1",
		},
	],
};