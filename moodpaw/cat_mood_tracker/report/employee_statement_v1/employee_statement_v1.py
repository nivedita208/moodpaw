# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"label": "Start Date", "fieldname": "start_date", "fieldtype": "Date", "width": 100},
        {"label": "End Date", "fieldname": "end_date", "fieldtype": "Date", "width": 100},
        {"label": "Working Days", "fieldname": "total_working_days", "fieldtype": "Float", "width": 160},
        {"label": "Basic", "fieldname": "basic", "fieldtype": "Currency", "width": 100},
        {"label": "HRA", "fieldname": "hra", "fieldtype": "Currency", "width": 100},
        {"label": "Net", "fieldname": "net_pay", "fieldtype": "Currency", "width": 120},
        {"label": "Total Deduction", "fieldname": "total_deduction", "fieldtype": "Currency", "width": 130},
        {"label": "Total Loans", "fieldname": "total_loan_repayment", "fieldtype": "Currency", "width": 130},
        {"label": "Net Salary", "fieldname": "rounded_total", "fieldtype": "Currency", "width": 150}
    ]

    data = get_salary_slip_data(filters)
    return columns, data

def get_salary_slip_data(filters): 
    where_clause = []
    values = []

    filters = filters or {}   # Ensures filters is a dictionary (avoid NoneType errors)

    # Apply filter conditions
    if filters.get("start_date"):
        where_clause.append("ss.start_date >= %s")
        values.append(filters["start_date"])

    if filters.get("end_date"):
        where_clause.append("ss.end_date <= %s")
        values.append(filters["end_date"])

    if filters.get("employee"):
        where_clause.append("ss.employee = %s")
        values.append(filters["employee"])

    if filters.get("currency"):
        where_clause.append("ss.currency = %s")
        values.append(filters["currency"])

    if filters.get("status"):
        status_map = {
            "Draft": 0,
            "Submitted": 1,
            "Cancelled": 2
        }
        where_clause.append("ss.docstatus = %s")
        values.append(status_map[filters["status"]])

    # Combine all conditions
    conditions_sql = " AND ".join(where_clause)
    if conditions_sql:
        conditions_sql = "WHERE " + conditions_sql

    # Final query
    query = f"""
        SELECT
            ss.start_date,
            ss.end_date,
            ss.total_working_days,
            ss.net_pay,
            ss.total_deduction,
            ss.total_loan_repayment,
            ss.rounded_total,
            MAX(CASE WHEN sse.salary_component = 'Basic' THEN sse.amount ELSE 0 END) AS basic,
            MAX(CASE WHEN sse.salary_component = 'House Rent Allowance' THEN sse.amount ELSE 0 END) AS hra
        FROM
            `tabSalary Slip` ss
        LEFT JOIN 
            `tabSalary Detail` sse 
             ON ss.name = sse.parent AND sse.parentfield = 'earnings'
        {conditions_sql}
        GROUP BY
            ss.name
        ORDER BY
            ss.start_date DESC
    """

    return frappe.db.sql(query, values, as_dict=True)

#   LEFT JOIN  : Join Salary Detail table to Salary Slip, linking child records (earnings only)
#  `tabSalary Detail` sse ON ss.name = sse.parent AND sse.parentfield = 'earnings':--- Use LEFT JOIN to include all Salary Slips even if they don't have matching earnings
# LEFT JOIN :--- Returns all records from the left table, and matched records from the right. If no match, shows NULL.
# Why use get() instead of filters["employee"]?
# filters.get("employee") → Returns None if the filter is not passed (no error).

# filters["employee"] → Gives KeyError if the filter was not selected by the user.

# status_map is a mapping between status names and internal database codes.
# It's needed because UI filter gives names like "Submitted", but SQL needs numbers like 1.
# values.append(status_map[filters["status"]]) ensures correct value goes into SQL query.
