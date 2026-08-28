
frappe.listview_settings['Doctor'] = {
    onload: function(listview) {
        listview.page.add_inner_button('Quick Create Doctor', function() {
            let dialog = new frappe.ui.Dialog({
                title: 'Create New Doctor',
                fields: [
                    {
                        label: 'Doctor Name',
                        fieldname: 'doctor_name',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Create Doctor',
                primary_action(values) {
                    frappe.call({
                        method: 'hospital.hospital.api.create_doctor',
                        args: {
                            doctor_name: values.doctor_name
                        },
                        callback: function(response) {
                            dialog.hide();
                            frappe.msgprint({
                                title: 'Success',
                                message: `Doctor <b>${response.message}</b> created successfully!`,
                                indicator: 'green'
                            });
                            listview.refresh();
                        }
                    });
                }
            });
            dialog.show();
        });
    }
};

// frappe.ui.form.on('Doctor', {

//     get_email_recipient_filters(frm, field) {

//         if (field === "bcc") {

//             return [
//                 [
//                     "Dynamic Link",
//                     "link_doctype",
//                     "=",
//                     "Doctor"
//                 ],
//                 [
//                     "Dynamic Link",
//                     "link_name",
//                     "=",
//                     frm.doc.name
//                 ]
//             ];

//         }

//     },
    
   


//     get_email_recipients(frm, field) {

//         if (field === "bcc") {

//             if (frm.doc.email) {
//                 return [frm.doc.email];
//             }

//             return [];
//         }

//     }

// });


//frm.set_query example  in Form Script  -- > Works only on the link field
// This code below sets a filter on the "department" field in the "Doctor" doctype, so that only departments with names containing "Cardiology" are shown in the dropdown.
// apps/hospital/hospital/hospital/doctype/doctor/doctor.js
// frappe.ui.form.on("Doctor", {
//     setup(frm) {
//         frm.set_query('department', () => {
//             return {
//                 filters: {
//                     name: ['not in', [
//                         'Accounts - TT', 'Marketing - TT', 'Sales - TT',
//                         'Purchase - TT', 'Operations - TT', 'Production - TT',
//                         'Dispatch - TT', 'Customer Service - TT', 'Human Resources - TT',
//                         'Management - TT', 'Quality Management - TT',
//                         'Research & Development - TT'
//                     ]]
//                 }
//             }
//         })
//     }
// })



// frm. call example in Form Script  -- > Works only on the link field
// frappe.ui.form.on("Doctor", {
//     refresh(frm) {
//         frm.add_custom_button('View Upcoming Schedule', () => {
//             frm.call('get_upcoming_schedule')
//                 .then(r => {
//                     if (r.message && r.message.length > 0) {
//                         let rows = r.message.map(s =>
//                             `<tr><td>${s.schedule_date}</td><td>${s.start_time}</td><td>${s.end_time}</td></tr>`
//                         ).join('');

//                         frappe.msgprint({
//                             title: 'Upcoming Schedule',
//                             message: `<table class="table"><tr><th>Date</th><th>Start</th><th>End</th></tr>${rows}</table>`
//                         });
//                     } else {
//                         frappe.msgprint('No upcoming schedule found.');
//                     }
//                 });
//         });
//     }
// });

// CONTROL -- Make control 

// frappe.ui.form.on("Doctor", {
//     refresh(frm) {
//         frm.add_custom_button('Show Due Date Field', () => {
//             let d = new frappe.ui.Dialog({
//                 title: 'Custom Control Example'
//             });

//             let $wrapper = $(d.body);
//             $wrapper.append('<div class="my-control"></div>');

//             let control = frappe.ui.form.make_control({  
//                 parent: $wrapper.find('.my-control'),
//                 df: {
//                     label: 'Exp',
//                     fieldname: 'exp',
//                     fieldtype: 'Data'
//                 },
//                 render_input: true
//             });

//             d.set_primary_action('Confirm', () => {
//                 let selected_date = parseInt(control.get_value(),10);
//                 if (!selected_date) {
//                     frappe.msgprint('Please select a date first.');
//                     return;
//                 }
//                 frm.set_value('experience', selected_date);
//                 frm.save();
//                 d.hide();
//             });

//             d.show();
//         });
//     }
// });

// frappe.listview_settings['Doctor'] = {
//     // Fetch these extra fields alongside the default list columns
//     add_fields: ['department', 'available', 'experience', 'consultation_fee'],

//     // Only show doctors marked available, by default
//     filters: [
//         ['available', '=', 1]
//     ],

//     hide_name_column: true,
//     hide_name_filter: false,

//     onload(listview) {
//         console.log('Doctor list loaded');
//     },

//     before_render() {
//         console.log('Doctor list about to render');
//     },

//     has_indicator_for_draft: false,

//     get_indicator(doc) {
//         if (doc.available) {
//             return [__("Available"), "green", "available,=,1"];
//         } else {
//             return [__("Unavailable"), "red", "available,=,0"];
//         }
//     },

//     primary_action() {
//         frappe.new_doc('Doctor');
//     },

//     get_form_link(doc) {
//         return `/app/doctor/${doc.name}`;
//     },

//     button: {
//         show(doc) {
//             return doc.available;
//         },
//         get_label() {
//             return 'Book';
//         },
//         get_description(doc) {
//             return __('Book appointment with {0}', [doc.doctor_name]);
//         },
//         action(doc) {
//             frappe.new_doc('Doctor Schedule', {
//                 doctor: doc.name
//             });
//         }
//     },

//     formatters: {
//         doctor_name(val) {
//             return val ? val.bold() : val;
//         },
//         consultation_fee(val) {
//             return val ? `₹${val}` : '-';
//         },
//         experience(val) {
//             return val ? `${val} yrs` : 'New';
//         }
//     }
// }