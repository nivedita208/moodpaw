// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expense Breakdown Report"] = {
	"filters": [
		{
			fieldname: "posting_date",
            label: "Posting Date",
            fieldtype: "Date",
            reqd: 1,
			default: frappe.datetime.year_start()

		},
		
		{
			fieldname: "expense_account",
			label: "Expense Account",
			fieldtype: "Link",
			options: "Account"
		  },

		  {
            fieldname: "status",
            label: "Status",
            fieldtype: "Select",
            options: "\nDraft\nSubmitted\nCancelled"
        }
		  
	]
};
