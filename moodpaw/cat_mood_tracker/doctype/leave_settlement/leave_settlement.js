// Copyright (c) 2025, meoww and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave Settlement", {
    refresh:function(frm){
        frm.add_custom_button(__("Create Payroll Entry"),function(){
            // validation : only create payroll entry if ls is submitted
            if (frm.doc.docstatus !== 1) {
                frappe.msgprint("Please submit the Leave Settlement before creating a Payroll Entry.");
                return;
            }
        // used for popup message
           frappe.confirm("Do you want to create a new Payroll Entry?",
            function(){
                // Yes callback – you can call server method here
                frappe.call({
                    method: "moodpaw.cat_mood_tracker.doctype.leave_settlement.leave_settlement.create_payroll_entry" ,// path of python function (appname.path.to.function)
                    args: { //It sends data (arguments) from the Leave Settlement form (frm) to the backend (Python method).
                        // employee,from_date,to_date(these are key name used in args dict which are used in python code as arguments)
                        employee: frm.doc.employee, 
                        from_date:frm.doc.from_date, 
                        to_date:frm.doc.to_date,
                        leave_settlement: frm.doc.name 
                    }, 
                    callback: function(serverReply) {                       
                        //frappe.msgprint("Payroll Entry Created:" + serverReply.message);
                        if(serverReply.message.startsWith("Payroll Entry already exist")){
                            frappe.msgprint(serverReply.message);
                        }
                        else{
                            frappe.msgprint("Payroll Entry Created:" + serverReply.message);
                            frm.reload_doc(); // to show the new linked entryrefresh to show the new linked payroll entry
                        }
                        
                       
                       console.log(serverReply);
                       console.log(serverReply.message);
                    }
                })

            },
            function(){
                // No callback – optional
               frappe.msgprint("Oops not in the mood to create new payroll entry! no problem")
            }

           )

        }
        ,"", // No group
         "btn-primary" //Blue color
    )
    }, 
}
);

 // after_save: function(frm) {
    //     if (frm.doc.docstatus === 1) {
    //         // This only runs after submit
    //         frappe.set_route("Form", "Employee", frm.doc.employee);
    //     }
    // },

	// refresh: function(frm) {
    //     if (frm.doc.docstatus === 2) {
    //         // If document is cancelled (docstatus == 2)
    //         frappe.set_route("Form", "Employee", frm.doc.employee);
    //     }
    // }

