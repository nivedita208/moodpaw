import frappe

def validate_spiritual_log(doc, method):
    frappe.msgprint(f"Hook triggered: method name is: {method}")
    valid_statuses = ("Pending", "Done", "Skipped")

    summary = {}
    completed = 0

    for task in doc.spiritual_task:
        if task.status not in valid_statuses:
            frappe.throw(f"Please Select the task name")

        summary[task.task_name] = task.status

        if task.status == "Done":
            completed = completed + 1

    doc.total_tasks = len(doc.spiritual_task)
    doc.tasks_summary = ", ".join([f"{k} : {v}" for k, v in summary.items()])

    frappe.msgprint(f"{completed} out of {doc.total_tasks} tasks completed today.")




    # #  1. Define valid statuses (Tuple - fixed values that should not change)
    # valid_statuses = ("Pending", "Done", "Skipped")  #  Tuple of allowed values

    # #  2. Create a dictionary to store task summary
    # summary = {}  # This will hold task_name: status
    # completed = 0  # Counter to count tasks marked as "Done"

    # #  Loop through each row in the child table (spiritual_tasks is a list)
    # for task in doc.spiritual_tasks:
    #     # If the status is not in allowed values, show error
    #     if task.status not in valid_statuses:
    #         frappe.throw(f"Invalid status in task: {task.task_name}")

    #     #  3. Add task name and its status to the dictionary
    #     summary[task.task_name] = task.status  # Ex: "Reading" : "Done"

    #     #  Count if task was done
    #     if task.status == "Done":
    #         completed += 1

    # # 4. Store total number of tasks using len()
    # doc.total_tasks = len(doc.spiritual_tasks)  # len() counts list items

    # # 5. Build a summary string from the dictionary and assign it to the doc
    # # Example: "Reading : Done, Meditation : Pending"
    # doc.tasks_summary = ", ".join([f"{k} : {v}" for k, v in summary.items()])

    # # Show message with how many tasks are done
    # frappe.msgprint(f"{completed} out of {doc.total_tasks} tasks completed today.")
