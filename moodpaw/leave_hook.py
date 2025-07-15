import frappe

def on_leave_submit(doc, method):
    if doc.employee:
        # Fetch the Employee document
        emp_doc = frappe.get_doc("Employee", doc.employee)

        # Update the fields safely
        emp_doc.custom_employee_status = "On Leave"
        emp_doc.custom_rejoin_date = None

        # Save and reload to reflect updates properly
        emp_doc.save(ignore_version=True)
        emp_doc.reload()

        # Show confirmation message
        frappe.msgprint(
            f"""
            <p>
            Employee <b>{emp_doc.employee_name}</b> marked as <b>On Leave</b> 
            .
            </p>
            """,
            title="Status Updated"
        )

def on_leave_cancel(doc, method):
    if doc.employee:
        # Fetch the full Employee document
        emp_doc = frappe.get_doc("Employee", doc.employee)

        # Update fields safely
        emp_doc.custom_employee_status = "Active"
        emp_doc.custom_rejoin_date = None

        # Save and reload to reflect changes
        emp_doc.save(ignore_version=True)
        emp_doc.reload()

        # Show message
        frappe.msgprint(
            f"""
            <p>
            Leave Application for <b>{emp_doc.employee_name}</b> cancelled.<br>
            Status reset to <b>Active</b>.
            </p>
            """,
            title="Status Updated"
        )
