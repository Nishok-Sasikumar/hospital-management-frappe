import os
import frappe
from frappe.modules import get_module_path, scrub
def create_web_view_templates(doc, method=None):
    """Create custom-branded HTML templates for doctypes with Has Web View enabled."""

    if doc.custom or doc.istable:
        return

    if not doc.has_web_view:
        return

    try:
        module_path = get_module_path(doc.module)
    except Exception:
        return

    doctype_folder = os.path.join(module_path, "doctype", scrub(doc.name))
    templates_path = os.path.join(doctype_folder, "templates")

    if not os.path.exists(doctype_folder):
        return  # doctype folder not created yet

    if not os.path.exists(templates_path):
        os.makedirs(templates_path)

    files = {
        scrub(doc.name) + ".html": f"""{{%- extends "templates/web.html" -%}}

{{% block page_content %}}
<h1>{{{{ doc.name }}}}</h1>
<!-- {doc.name} detail page -->
{{% endblock %}}
""",
        scrub(doc.name) + "_row.html": f"""<div class="{scrub(doc.name)}-row">
	<!-- {doc.name} list row template -->
</div>
""",
    }

    for filename, content in files.items():
        file_path = os.path.join(templates_path, filename)
        if os.path.exists(file_path):
            continue  # don't overwrite existing customizations
        with open(file_path, "w") as f:
            f.write(content)




def create_list_js_boilerplate(doc, method=None):
    # Only for doctypes belonging to your own app/module, skip core/other apps
    if doc.custom or doc.istable:
        return

    try:
        module_path = get_module_path(doc.module)
    except Exception:
        return

    folder_path = os.path.join(module_path, "doctype", scrub(doc.name))
    file_path = os.path.join(folder_path, scrub(doc.name) + "_list.js")

    if os.path.exists(file_path):
        return  # don't overwrite existing file

    if not os.path.exists(folder_path):
        return  # doctype folder not created yet (shouldn't normally happen)

    boilerplate = f"""frappe.listview_settings['{doc.name}'] = {{
	add_fields: [],
	get_indicator: function(doc) {{

	}},
}};
"""

    with open(file_path, "w") as f:
        f.write(boilerplate)