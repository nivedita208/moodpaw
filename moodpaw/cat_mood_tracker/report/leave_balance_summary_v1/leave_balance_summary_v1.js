// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Leave Balance Summary v1"] = {
	"filters": [
		{
            "fieldname": "employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "leave_type",
            "label": "Leave Type",
            "fieldtype": "Link",
            "options": "Leave Type"
        },
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
			"reqd":1,
			"default": frappe.datetime.year_start()
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date"
        },
        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nOpen\nApproved\nRejected\nCancelled"
        }
	]
};



