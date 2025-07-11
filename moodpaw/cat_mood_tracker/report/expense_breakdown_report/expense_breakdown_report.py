# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    columns = [
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 100},
        {"label": "Voucher No", "fieldname": "voucher_no", "fieldtype": "Link", "options": "Journal Entry", "width": 180},
        {"label": "Account", "fieldname": "account", "fieldtype": "Link", "options": "Account", "width": 200},
        {"label": "Debit", "fieldname": "debit", "fieldtype": "Currency", "width": 90},
        {"label": "Credit", "fieldname": "credit", "fieldtype": "Currency", "width": 90},
        {"label": "Remark", "fieldname": "remark", "fieldtype": "Small Text", "width": 150},
        {"label": "Total Debit", "fieldname": "total_debit", "fieldtype": "Currency", "width": 120},
        {"label": "Total Credit", "fieldname": "total_credit", "fieldtype": "Currency", "width": 120},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
    ]
    data = expense_breakdown_data(filters)
    return columns, data

def expense_breakdown_data(filters):
    where_clause = []
    values = []

    filters = filters or {}  # Avoid NoneType errors

    # Filter: Posting Date
    if filters.get("posting_date"):
        where_clause.append("je.posting_date >= %s")
        values.append(filters.get("posting_date"))

    # Filter: Expense Account
    if filters.get("expense_account"):
        where_clause.append("jea.account = %s")
        values.append(filters.get("expense_account"))

    # Filter: Status
    if filters.get("status"):
        status_map = {
            "Draft": 0,
            "Submitted": 1,
            "Cancelled": 2
        }
        where_clause.append("je.docstatus = %s")
        values.append(status_map.get(filters.get("status")))

    # Combine conditions
    conditions = " AND ".join(where_clause)
    if conditions:
        conditions = "WHERE " + conditions

    query = f"""
        SELECT
            je.posting_date,
            je.name AS voucher_no,
            jea.account,
            jea.debit,
            jea.credit,
            je.remark,
            CASE WHEN jea.idx = 1 THEN je.total_debit ELSE NULL END AS total_debit,
            CASE WHEN jea.idx = 1 THEN je.total_credit ELSE NULL END AS total_credit,
            CASE WHEN jea.idx = 1 THEN je.total_amount ELSE NULL END AS total_amount
        FROM
            `tabJournal Entry` je
        JOIN
            `tabJournal Entry Account` jea ON je.name = jea.parent
        {conditions}
        ORDER BY
            je.posting_date DESC, jea.idx ASC
    """

    return frappe.db.sql(query, values, as_dict=True)





