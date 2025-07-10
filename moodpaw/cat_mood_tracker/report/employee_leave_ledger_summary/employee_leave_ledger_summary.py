# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{"label": "From Date", "fieldname": "from_date", "fieldtype": "Date", "width": 100},
		{"label": "To Date", "fieldname": "to_date", "fieldtype": "Date", "width": 100},
		{"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 180},
		{"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 130},
		{"label": "Leave Type", "fieldname": "leave_type", "fieldtype": "Link", "options": "Leave Type", "width": 160},
		{"label": "Transaction Type", "fieldname": "transaction_type", "fieldtype": "Data", "width": 150},
		#{"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
		{"label": "Leaves", "fieldname": "leaves", "fieldtype": "Float", "width": 100},
	]

	data = employee_leave_ledger_data(filters)
	return columns, data

def employee_leave_ledger_data(filters):
	where_clause = []
	values = []

	# Apply filter logic
	if filters.get("from_date"):
		where_clause.append("lle.from_date >= %s")
		values.append(filters["from_date"])
	if filters.get("to_date"):
		where_clause.append("lle.to_date <= %s")
		values.append(filters["to_date"])
	if filters.get("employee"):
		where_clause.append("lle.employee = %s")
		values.append(filters["employee"])
	if filters.get("leave_type"):
		where_clause.append("lle.leave_type = %s")
		values.append(filters["leave_type"])

	if filters.get("transaction_type"):
		where_clause.append("lle.transaction_type = %s")
		values.append(filters["transaction_type"])

	# Combine all conditions
	logic = " AND ".join(where_clause)
	if logic:
		logic = "WHERE " + logic

	# Final query
	query = f"""
		SELECT
			lle.from_date,
			lle.to_date,
			lle.employee,
			lle.employee_name,
			lle.leave_type,
			lle.transaction_type,
			
			lle.leaves
		FROM
			`tabLeave Ledger Entry` lle
		{logic}
		ORDER BY
			lle.from_date DESC
	"""

	return frappe.db.sql(query, values, as_dict=True)


