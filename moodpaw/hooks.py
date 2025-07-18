app_name = "moodpaw"
app_title = "Cat Mood Tracker"
app_publisher = "meoww"
app_description = "Track my cat\'s daily moods"
app_email = "meow12@gmgmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
doc_events = {
    "Leave Application": {
        "on_submit": "moodpaw.leave_hook.on_leave_submit",
        "on_cancel": "moodpaw.leave_hook.on_leave_cancel"
    }
}

doc_events = {
    "Timesheet": {
        "on_submit": "moodpaw.snack_hooks.create_snack_request_if_overtime"
    }
}

doc_events = {
    "Spiritual Task Log": {
        "validate": "moodpaw.practice_hooks.spiritual_task_hooks.validate_spiritual_log"
    }
}
# include js, css files in header of desk.html
# app_include_css = "/assets/moodpaw/css/moodpaw.css"
# app_include_js = "/assets/moodpaw/js/moodpaw.js"

# include js, css files in header of web template
# web_include_css = "/assets/moodpaw/css/moodpaw.css"
# web_include_js = "/assets/moodpaw/js/moodpaw.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "moodpaw/public/scss/website"

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "moodpaw.utils.jinja_methods",
# 	"filters": "moodpaw.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "moodpaw.install.before_install"
# after_install = "moodpaw.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "moodpaw.uninstall.before_uninstall"
# after_uninstall = "moodpaw.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "moodpaw.utils.before_app_install"
# after_app_install = "moodpaw.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "moodpaw.utils.before_app_uninstall"
# after_app_uninstall = "moodpaw.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "moodpaw.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"moodpaw.tasks.all"
# 	],
# 	"daily": [
# 		"moodpaw.tasks.daily"
# 	],
# 	"hourly": [
# 		"moodpaw.tasks.hourly"
# 	],
# 	"weekly": [
# 		"moodpaw.tasks.weekly"
# 	],
# 	"monthly": [
# 		"moodpaw.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "moodpaw.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "moodpaw.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "moodpaw.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["moodpaw.utils.before_request"]
# after_request = ["moodpaw.utils.after_request"]

# Job Events
# ----------
# before_job = ["moodpaw.utils.before_job"]
# after_job = ["moodpaw.utils.after_job"]

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
# 	"moodpaw.auth.validate"
# ]
