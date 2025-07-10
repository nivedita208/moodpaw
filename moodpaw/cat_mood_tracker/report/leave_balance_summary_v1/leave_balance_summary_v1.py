# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 170},
        {"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 150},
        {"label": "Leave Type", "fieldname": "leave_type", "fieldtype": "Link", "options": "Leave Type", "width": 120},
        {"label": "From Date", "fieldname": "from_date", "fieldtype": "Date", "width": 100},
        {"label": "To Date", "fieldname": "to_date", "fieldtype": "Date", "width": 100},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
        {"label": "Leave Days", "fieldname": "total_leave_days", "fieldtype": "Float", "width": 100}
    ]

    data = get_leave_application_data(filters)
    return columns, data

def get_leave_application_data(filters):
    where_clause = []
    values = []

    # Apply filter conditions
    if filters.get("employee"):
        where_clause.append("la.employee = %s")
        values.append(filters.get("employee"))

    if filters.get("leave_type"):
        where_clause.append("la.leave_type = %s")
        values.append(filters.get("leave_type"))

    if filters.get("from_date"):
        where_clause.append("la.from_date >= %s")
        values.append(filters.get("from_date"))

    if filters.get("to_date"):
        where_clause.append("la.to_date <= %s")
        values.append(filters.get("to_date"))

    if filters.get("status"):
        where_clause.append("la.status = %s")
        values.append(filters.get("status"))

    # Combine all conditions
    conditions = " AND ".join(where_clause)
    if conditions:
        conditions = "WHERE " + conditions

    # Final query
    query = f"""
        SELECT 
            la.employee,
            e.employee_name,
            la.leave_type,
            la.from_date,
            la.to_date,
            la.status,
            la.total_leave_days
        FROM 
            `tabLeave Application` la
        LEFT JOIN 
            `tabEmployee` e ON la.employee = e.name
        {conditions}
        ORDER BY 
            la.from_date DESC
    """

    return frappe.db.sql(query, values, as_dict=True)





		


