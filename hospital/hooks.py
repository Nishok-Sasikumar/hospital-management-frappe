app_name = "hospital"
app_title = "Hospital"
app_publisher = "Nishok"
app_description = "Hospital Management System"
app_email = "nishok2005kuro@gmail.com"
app_license = "mit"



# hooks.pyx
# Apps
# ------------------

# additional_timeline_content: {
#     "ToDo": ["hospital.timeline.todo_timeline"]
# }


# base_template_map = {
#     r"docs.*": "templates/doc_base.html",
# }
# has_permission = {
#     "Cus_1": "hospital.permissions.cus_1_has_permission",
# }
# fixtures = [
#     {
#         "dt": "Property Setter",
#         "filters": [["doc_type", "in", ["Cus 1", "Event Notifications"]]]
#     },
#     {
#         "dt": "Custom Field",
#         "filters": [["dt", "in", ["Cus 1", "Event Notifications"]]]
#     }
# ]



# extend_doctype_class = {
#     "Doctor": ["hospital.extensions.doctor.DoctorMixin"],
# }



# on_login = "hospital.overrides.successful_login"
# on_session_creation = "app.overrides.allocate_free_credits"
# on_logout = "app.overrides.clear_user_cache"

# doctype_js = {
#     "ToDo": "public/js/todo.js",
# }

# auto_cancel_exempted_doctypes = ["Patient Apointment"]



# web_include_js = "assets/hospital/js/app.js"
# web_include_css = "assets/hospital/css/app.css"



# after_build = "studio.build.after_build"



# website_redirects = [
#     {"source": "/compare", "target": "/comparison"},
#     {"source": "/docs(/.*)?", "target": "https://docs.tennismart.com\\1"},
#     {"source": r"/items/item\?item_name=(.*)", "target": "/items/\\1", "match_with_query_string": True},
# ]   

# website_route_rules = [
#     {"from_route": "/items/<item_name>", "to_route": "items"},
# ]
   

# extend_website_page_controller_context = {
#     "frappe.www.404": "hospital.templates.context_404"
# }

# website_context = {
#     "favicon": "/assets/app/image/favicon.png",
#     "splash_image": "/assets/app/image/splash.png"
# }

# update_website_context = "app.overrides.website_context"

# webform_include_js = {"Nishok": "public/js/custom_todo.js"}
# webform_include_css = {"Nishok": "public/css/custom_todo.css"}

# ignore_links_on_delete = ["Doctor Schedule"]

# hospital/hospital/hooks.py
# signup_form_template = "hospital/templates/signup-form.html"
# app/hooks.py
# website_context = {
#     "favicon": "/assets/hospital/image/Wallpaper.png"
# }
# update_website_context = "app.overrides.website_context"



# sounds = [
#     {"name": "ping", "src": "/assets/hospital/sounds/error.mp3", "volume": 1}
# ]



# web_include_js = "/assets/hospital/js/app.js"
# web_include_css = "/assets/hospital/css/app.css"



# webform_include_js = {"nishok": "/assets/hospital/js/custom_todo.js"}
# webform_include_css = {"nishok": "/assets/hospital/css/custom_todo.css"}



# hospital/hospital/hooks.py

# extend_website_page_controller_context = {
#     "frappe.www.404": "hospital.pages.context_404",
#     "frappe.www.about": "hospital.pages.context_about"
# }
# python module path
# extend_bootinfo = "hospital.boot.boot_session"

# hospital/hospital/hooks.py

# brand_html = '<div><img src="/assets/hospital/image/Wallpaper.png" style="height: 30px; margin-right: 5px;"> Nishok</div>'

# hospital/hooks.py



user_data_fields = [
    {
        "doctype": "Patient",
        "filter_by": "email",
        "redact_fields": ["phone"],
    },
]

# send_sms = "hospital.overrides.sms.send_sms"
# send_token_via_sms = "hospital.overrides.sms.send_token_via_sms"
# app_logo_url ="Cover.png"
# app_title = "Hospital"

calendars = ["Cus_1","Doctor"]

# after_build = "hospital.build.after_build"
# before_migrate = "hospital.migrate.before_migrate"
# after_migrate = "hospital.migrate.after_migrate"

# website_clear_cache = "hospital.website.clear_cache"

# hospital/hooks.py

# doc_events = {
#     "Patient": {
#         "before_naming": "hospital.hospital.patient_lifecycle.custom_before_naming",
#         "autoname": "hospital.hospital.patient_lifecycle.custom_autoname",
#         "before_insert": "hospital.hospital.patient_lifecycle.set_default_patient_data",
#         "validate": "hospital.hospital.patient_lifecycle.validate_patient_info",
#         "before_save": "hospital.hospital.patient_lifecycle.final_patient_cleanup",
#         "after_insert": "hospital.hospital.patient_lifecycle.log_new_patient_creation"
#     }
# }



# doc_events = {
#     "Patient": {
#         "validate": "hospital.hospital.api.custom_logic"
#     }
# }
# app_include_js = "custom_desk.bundle.js"
# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "hospital",
# 		"logo": "/assets/hospital/logo.png",
# 		"title": "Hospital",
# 		"route": "/hospital",
# 		"has_permission": "hospital.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hospital/css/hospital.css"
# app_include_js = "/assets/hospital/js/hospital.js"

# include js, css files in header of web template
# web_include_css = "/assets/hospital/css/hospital.css"
# web_include_js = "/assets/hospital/js/hospital.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hospital/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hospital/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hospital.utils.jinja_methods",
# 	"filters": "hospital.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hospital.install.before_install"
# after_install = "hospital.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hospital.uninstall.before_uninstall"
# after_uninstall = "hospital.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hospital.utils.before_app_install"
# after_app_install = "hospital.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hospital.utils.before_app_uninstall"
# after_app_uninstall = "hospital.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "hospital.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hospital.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hospital.tasks.all"
# 	],
# 	"daily": [
# 		"hospital.tasks.daily"
# 	],
# 	"hourly": [
# 		"hospital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hospital.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hospital.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hospital.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "hospital.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hospital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hospital.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hospital.utils.before_request"]
# after_request = ["hospital.utils.after_request"]

# Job Events
# ----------
# before_job = ["hospital.utils.before_job"]
# after_job = ["hospital.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hospital.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
#export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

