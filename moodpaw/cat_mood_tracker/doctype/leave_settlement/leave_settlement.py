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

#################################   custom button code ##############

# whitelisted function must be outside the class
@frappe.whitelist() # it is required to connect .py code with js(frappe.call) 
def create_payroll_entry(employee, from_date, to_date, leave_settlement):
    try:
        # get leave settlement doc
        existing = frappe.get_doc("Leave Settlement", leave_settlement)

        #check if already exist
        if existing.payroll_entry:
            return f"Payroll Entry already exist: {existing.payroll_entry}"


        # create new payroll entry document
        pe = frappe.new_doc("Payroll Entry")
        pe.company = frappe.defaults.get_user_default("Company")  # Default company
        payable_account = frappe.db.get_value("Company", pe.company, "default_payroll_payable_account") #default payroll_payable_account
        # Fetch default payroll payable account from that company
        # Set payroll payable account
        pe.payroll_payable_account = payable_account
        pe.exchange_rate = 1.0
        pe.payroll_frequency = "Monthly"
        pe.start_date = from_date
        pe.end_date = to_date
        

        # Add employee to child table
        pe.append("employees",{ #here employess -- it’s the fieldname of the child table field inside Payroll Entry
            "employee": employee #Put the value from the variable employee into the field named "employee" in the child table row.
        }
           )

        pe.insert()

        # link back to leave settlement if pe exist
        existing.payroll_entry = pe.name
        existing.save()

        return pe.name
        
    except Exception as e:   
        # Exception as e -->holds the actual error message 
        frappe.throw(f" Something went wrong: {e}")
       

    # if i want to return name and status 
    # return {
#     "name": pe.name,
#     "status": pe.status
# }

    



   
