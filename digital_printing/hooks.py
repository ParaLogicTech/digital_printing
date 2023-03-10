from . import __version__ as app_version

app_name = "digital_printing"
app_title = "Digital Printing"
app_publisher = "ParaLogic"
app_description = "Digital Printing ERP Application"
app_email = "info@paralogic.io"
app_license = "GNU General Public License (v3)"
required_apps = ["erpnext"]

after_install = "digital_printing.install.after_install"

override_doctype_class = {
	"Item": "digital_printing.overrides.item_hooks.ItemDP"
}

doctype_js = {"Item" : "overrides/item_hooks.js"}

update_item_override_fields = "digital_printing.overrides.item_hooks.update_item_override_fields"

fixtures = [
	{
		"doctype": "Custom Field",
		"filters": {
			"name": ["in", [
				'Item-print_item_type',
				'Item-printing_tab',
				'Item-sec_design_properties',
				'Item-design_name',
				'Item-design_width',
				'Item-design_height',
				'Item-column_break_9y2g0',
				'Item-design_uom',
				'Item-design_gap',
				'Item-per_wastage',
				'Item-column_break_mjbrg',
				'Item-process_item',
				'Item-design_notes',
				'Item-sec_fabric_properties',
				'Item-fabric_material',
				'Item-fabric_type',
				'Item-column_break_fb7ki',
				'Item-fabric_width',
				'Item-fabric_gsm',
				'Item-column_break_vknw6',
				'Item-fabric_construction',
				'Item-fabric_item',
				'Item-fabric_item_name',
				'Item Group-print_item_type',
				'Item Source-print_item_type',
				'Brand-print_item_type',
			]]
		}
	},
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/digital_printing/css/digital_printing.css"
# app_include_js = "/assets/digital_printing/js/digital_printing.js"

# include js, css files in header of web template
# web_include_css = "/assets/digital_printing/css/digital_printing.css"
# web_include_js = "/assets/digital_printing/js/digital_printing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "digital_printing/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "digital_printing.utils.jinja_methods",
#	"filters": "digital_printing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "digital_printing.install.before_install"
# after_install = "digital_printing.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "digital_printing.uninstall.before_uninstall"
# after_uninstall = "digital_printing.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "digital_printing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"digital_printing.tasks.all"
#	],
#	"daily": [
#		"digital_printing.tasks.daily"
#	],
#	"hourly": [
#		"digital_printing.tasks.hourly"
#	],
#	"weekly": [
#		"digital_printing.tasks.weekly"
#	],
#	"monthly": [
#		"digital_printing.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "digital_printing.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "digital_printing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "digital_printing.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"digital_printing.auth.validate"
# ]
