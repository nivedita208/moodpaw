// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Leave Ledger Summary"] = {
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
            fieldname: "employee",
            label: "Employee",
            fieldtype: "Link",
            options: "Employee"
        },
        {
            fieldname: "leave_type",
            label: "Leave Type",
            fieldtype: "Link",
            options: "Leave Type"
        },
        
		{
   		 	fieldname: "transaction_type",
    		label: "Transaction Type",
    		fieldtype: "Select",
    		options: "\nLeave Allocation\nLeave Application\nLeave Encashment",
    		default: "Leave Application"
		}
	]
};
