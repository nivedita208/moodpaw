// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase Invoice Item Summary"] = {
	"filters": [
		{
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date",
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date",
            reqd: 1
        },
        {
            fieldname: "supplier",
            label: "Supplier",
            fieldtype: "Link",
            options: "Supplier"
        },
		{
			fieldname:"status",
			label:"Status",
			fieldtype: "Select",
			options: "\nDraft\nSubmitted\nCancelled"
		}
	]
};
