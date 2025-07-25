# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 100},
		{"label": "Invoice No", "fieldname": "invoice_no", "fieldtype": "Link", "options": "Purchase Invoice", "width": 100},
		{"label": "Supplier", "fieldname": "supplier", "fieldtype": "Link", "options": "Supplier", "width": 150},
		{"label": "Item", "fieldname": "item", "fieldtype": "Data", "width": 100},
		{"label": "Qty", "fieldname": "qty", "fieldtype": "Int", "width": 80},
		{"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 100},
		{"label": "Total Invoice Amount", "fieldname": "total_invoice_amount", "fieldtype": "Currency", "width": 200}
	]

	data = get_purchase_invoice_item_data(filters)
	return columns, data

def get_purchase_invoice_item_data(filters):
	where_clause = []
	values = []

	if filters.get("from_date"):
		where_clause.append("pi.posting_date >= %s")
		values.append(filters.get("from_date"))

	if filters.get("to_date"):
		where_clause.append("pi.posting_date <= %s")
		values.append(filters.get("to_date"))

	if filters.get("supplier"):
		where_clause.append("pi.supplier = %s")
		values.append(filters.get("supplier"))

	if filters.get("status"):
		where_clause.append("pi.docstatus = %s")
		status_map = {
			"Draft": 0,
			"Submitted": 1,
			"Cancelled": 2
		}
		values.append(status_map.get(filters.get("status")))

	conditions = " AND ".join(where_clause)
	if conditions:
		conditions = "WHERE " + conditions

	query = f"""
		SELECT
			pi.posting_date AS date,
			pi.name AS invoice_no,
			pi.supplier,
			pii.item_name AS item,
			pii.qty,
			pii.amount,
			CASE WHEN pii.idx = 1 THEN pi.grand_total ELSE NULL END AS total_invoice_amount
		FROM
			`tabPurchase Invoice` pi
		LEFT JOIN
			`tabPurchase Invoice Item` pii ON pi.name = pii.parent
		{conditions}
		ORDER BY
			pi.posting_date DESC, pii.idx ASC
	"""

	return frappe.db.sql(query, values=values, as_dict=True)

