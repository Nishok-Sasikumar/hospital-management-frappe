// Copyright (c) 2026, Nishok and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Doctor", {
// 	refresh(frm) {

// 	},
// });
frappe.realtime.on('new_doctor_registered', (data) => {
    console.log('New doctor:', data.name, data.doctor_name, data.department);
});