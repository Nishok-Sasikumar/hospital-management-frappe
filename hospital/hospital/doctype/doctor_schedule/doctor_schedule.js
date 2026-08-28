// Copyright (c) 2026, Nishok and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Doctor Schedule", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Doctor Schedule', {
//     before_discard(frm) {
//         console.log("Before discard");
//     },
//     timeline_refresh(frm) {
//         console.log("Timeline refresh");
//     },
//     get_email_recipients(frm,fieldname) {
//         if (field === "recipients") {
//             return [frm.doc.custom_email];
//         }

//     }
// });

frappe.ui.form.on("Doctor Schedule", {
    onload(frm) {
        frm.ignore_doctypes_on_cancel_all = ["Doctor"];
    }
});