// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Statement v1"] = {
    "filters": [
        {
            fieldname: "start_date",
            label: "Start Date",
            fieldtype: "Date",
            reqd: 1,
            default: frappe.datetime.year_start() //it gives YYYY-MM-DD IN THIS FORMAT but frappe internally setting DD-MM-YYYY IN THIS format in report based on (indian format)
        },
        {
            fieldname: "end_date",
            label: "End Date",
            fieldtype: "Date"
        },
        {
            fieldname: "currency",
            label: "Currency",
            fieldtype: "Link",
            options: "Currency"
        },
        {
            fieldname: "employee",
            label: "Employee",
            fieldtype: "Link",
            options: "Employee"
        },
        {
            fieldname: "status",
            label: "Status",
            fieldtype: "Select",
            options: "\nDraft\nSubmitted\nCancelled"
        }
    ],

    
};
