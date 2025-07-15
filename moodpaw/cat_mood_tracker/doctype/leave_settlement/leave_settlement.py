# Copyright (c) 2025, meoww and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class LeaveSettlement(Document):

    def before_submit(self):
        allowed_status = ["Approved","Rejected"]
        if self.status not in allowed_status:
            frappe.throw(
                f"Only Leave Settlement with Status 'Approved'and'Rejected' can be Submitted.Current status: {self.status}",
                title="Message"
                )

    def on_submit(self):
        today = nowdate()
        if self.from_date <= today <= self.to_date:
            frappe.db.set_value("Employee", self.employee, {
                "custom_employee_status": "On Leave",
                "custom_rejoin_date": None
            })

            # To reload the employee doc
            emp_doc = frappe.get_doc("Employee",self.employee)
            emp_doc.reload()

            # Show message
            employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")
            frappe.msgprint(
                f"""
                
                Employee {employee_name} marked as On Leave.
                
                """,
                title="Status Updated"
            )

            
    def on_cancel(self):
        # Fetch Employee doc using Document API
            emp_doc = frappe.get_doc("Employee", self.employee)

            # Update fields safely
            emp_doc.custom_employee_status = "Active"
            emp_doc.custom_rejoin_date = None

    # Save and reload to apply changes and reflect them correctly
            emp_doc.save(ignore_version=True)
            emp_doc.reload()

    # Show confirmation message
            frappe.msgprint(
                f"""
                <p>
                Leave Settlement <b>{self.name}</b> Cancelled <br>
                Employee <b>{emp_doc.employee_name}</b> marked as <b>Active</b>.
                </p>
                """,
                title="Status Updated"
    )



   
