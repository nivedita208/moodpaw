# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class RejoinEntry(Document):
    def on_submit(self):
        # Get the Employee document
        emp_doc = frappe.get_doc("Employee", self.employee)

        # Update status and rejoin date directly
        emp_doc.custom_employee_status = "Active"
        emp_doc.custom_rejoin_date = self.rejoin_date

        # Save and reload the Employee doc
        emp_doc.save(ignore_version=True)
        emp_doc.reload()

        # Show confirmation message
        frappe.msgprint(
            f"""
            <p>
            Employee <b>{emp_doc.employee_name}</b> marked as <b>Active</b>.<br>
            Rejoin Date set to <b>{self.rejoin_date}</b>.
            </p>
            """,
            title="Status Updated"
        )

    



