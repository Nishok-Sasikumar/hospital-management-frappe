// Copyright (c) 2026, Nishok and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Cus_1", {
// 	refresh(frm) {

// 	},
// });



//child table script


// frappe.ui.form.on('Cus_1', {
//     refresh(frm) {
//         // This function will be called when the form is refreshed
//         console.log("Form refreshed");
//     }
// });
// frappe.ui.form.on('cus_child', {
//     new_name(frm,cdt,cdn){
//         let row = locals[cdt][cdn];
//         console.log("New Name changed to:", row.new_name);
//     },

// });
// frappe.ui.form.on("Cus_1", {
//  validate(frm) {
//         // This function will be called before the form is saved
//         frappe.msgprint("Form is being validated");
//     }





//Button script--------------------------->

//single button script --->
// frappe.ui.form.on("Cus_1", {
//     onload_post_render(frm) {
//         if (frm.is_new()) {
//             frm.add_custom_button("Patient", () => {
//                 frappe.set_route("List", "Patient");
//             });
//             frm.change_custom_button_type('Patient', null, 'danger');
//             frm.remove_custom_button('Patient'); //removed here 
//             frm.clear_custom_buttons(); //cleared all buttons 
//         }
//     }
    
// });




//Dropdown button script --->

// frappe.ui.form.on("Cus_1", {
//     onload_post_render(frm) {
//         if (frm.is_new()) {

//             frm.add_custom_button("Doctor", () => {
//                 frappe.set_route("List", "Doctor");
//             }, "Open Reference Form");

//             frm.add_custom_button("Patient", () => {
//                 frappe.set_route("List", "Patient");
//             }, "Open Reference Form");

//         }
//     }
// });




// frappe.ui.form.on("Cus_1", {
//     onload_post_render(frm) {
//         if (frm.is_new()) {

//             frm.add_custom_button("Doctor", () => {
//                 frappe.set_route("List", "Doctor");
//             }, "Open Reference Form");

//             frm.add_custom_button("Patient", () => {
//                 frappe.set_route("List", "Patient");
//             }, "Open Reference Form");

//         }
//     }
// });


// });




// frappe.ui.form.on("Cus_1", {
//     child_table_add(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];

//         console.log("Child row added:", row);

//         // Example:
//         row.new_name = "";
//         row.sec_new_name = "";

//         frm.refresh_field("child_table");
//     },

//     child_table_remove(frm, cdt, cdn) {
//         console.log("Child row removed:", cdn);

//         // Your logic after removing a row
//     },

//     child_table_move(frm, cdt, cdn) {
//         console.log("Child row moved:", cdn);

//         // Your logic after reordering rows
//     },

//     form_render(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];

//         console.log("Child row form rendered:", row);

//         // Logic when a child row is opened as a form
//     },

//     before_child_table_remove(frm, cdt, cdn) {
//         let row = locals[cdt][cdn];

//         console.log("Before removing:", row);

//         // Return false if you want to prevent deletion.
//         // return false;
//     }
// });




//Change docfield property script --->

// frappe.ui.form.on("Cus_1", {
//     onload(frm) {
//         frm.set_df_property("second_name", "read_only", 1);
//     }
// });





// Toogle the read-only property based on a condition, you can use the following code:

// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         let is_allowed = frappe.user_roles.includes("System Manager");

//         frm.toggle_enable(
//             ["second_name", "custom_name", "custom_barcode"],
//             is_allowed
//         );
//     }
// });




// set priority as mandatory
// frappe.ui.form.on("Cus_1", {
//     second_name(frm) {
//         frm.toggle_reqd('custom_barcode', frm.doc.select === '3');
//     }
// })



//hides the custom_barcode field when second_name is changed

// frappe.ui.form.on("Cus_1", {
//     second_name(frm) {
//         frm.toggle_display('custom_barcode');
//     }
// })



//Link fiels is required for frm.set_query -- check on the doctor doctype for this example


//Adding a new row to the child table when the button is clicked
// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         frm.add_custom_button('Add Sample Row', () => {
//             let row = frm.add_child('child_table', {
//                 new_name: 'Karim',
//                 sec_new_name: 'Dulquar'
//             });
//             frm.refresh_field('child_table');
//             frappe.show_alert('Row added!');
//         });
//     }
// });

//get_selected_children example in Form Script  -- > Works only on the child table
// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         frm.add_custom_button('Add Sample Row', () => {
//             let row = frm.add_child('child_table', {
//                 new_name: 'Karim',
//                 sec_new_name: 'Dulquar'
//             });
//             frm.refresh_field('child_table');
//         });

//         frm.add_custom_button('Delete Selected Rows', () => {
//             let selected = frm.get_selected();

//             if (!selected.child_table || selected.child_table.length === 0) {
//                 frappe.msgprint('No rows selected in the child table.');
//                 return;
//             }

//             selected.child_table.forEach((row_name) => {
//                 let row = frappe.get_doc('cus_child', row_name);
//                 frm.get_field('child_table').grid.grid_rows_by_docname[row_name].remove();
//             });

//             frm.refresh_field('child_table');
//             frappe.show_alert(`Removed ${selected.child_table.length} row(s)`);
//         });
//     }
// });

// form trigger example in Form Script  -- > Works only on the child table

// frappe.ui.form.on("Cus_1", {
//     second_name(frm) {
//         frm.trigger('setup_buttons');
//     },

//     setup_buttons(frm) {
//         frm.add_custom_button('Add Sample Row', () => {
//             frm.add_child('child_table', {
//                 new_name: 'Karim',
//                 sec_new_name: 'Dulquar'
//             });
//             frm.refresh_field('child_table');
//         });

//         frm.add_custom_button('Delete Selected Rows', () => {
//             let selected = frm.get_selected();

//             if (!selected.child_table || selected.child_table.length === 0) {
//                 frappe.msgprint('No rows selected in the child table.');
//                 return;
//             }

//             selected.child_table.forEach((row_name) => {
//                 frm.get_field('child_table').grid.grid_rows_by_docname[row_name].remove();
//             });

//             frm.refresh_field('child_table');
//             frappe.show_alert(`Removed ${selected.child_table.length} row(s)`);
//         });
//     }
// });


//frm.call example in Form Script  -- > Works only on the child table
// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         frm.add_custom_button('Add Sample Row', () => {
//             frm.call({
//                 method: 'add_sample_row',
//                 doc: frm.doc,
//                 callback: function(r) {
//                     if (r.message) {
//                         frm.refresh_field('child_table');
//                         frappe.show_alert('Row added!');
//                     }
//                 }
//             });
//         });
//     }
// });


// frappe.ui.form.make_control({

// })

// frappe.meta.docfield_map['sec_section'].fieldtype.formatter = (value) => {
//  if (value==='Section Break') return '🔵 Section Break';
//  else return value;
// }


// Scanner API:

// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         frm.add_custom_button('Scan QR Code', () => {
//             let scanned_codes = [];
//             new frappe.ui.Scanner({
//                 dialog: true,
//                 multiple: false,
//                 on_scan(data) {
//                     let code = data.decodedText;
//                     if (scanned_codes.includes(code)) {
//                         return;
//                     }
//                     scanned_codes.push(code);
//                     frm.set_value('second_name', scanned_codes.join(', '));
//                     frappe.show_alert({
//                         message: `QR Code scanned: ${code}`,
//                         indicator: 'green'
//                     });
//                 }
//             });
//         });
//     }
// });



frappe.ui.form.on("Cus_1", {
    refresh(frm) {
        frm.add_custom_button('Scan QR Code', () => {
            let x ="" ;
             new frappe.ui.Scanner({
                dialog: true,
                multiple: true,
                on_scan(data) {
                    x+=data.decodedText;
                    console.log(x);
                    frm.set_value('second_name',x);
                    frm.save();
                    // frappe.show_alert(`QR Code scanned: ${data.decodedText}`);
                }
            });
        });
    }
});
// frappe.ui.form.on("Cus_1",{
//     refresh(frm){
//       frappe.prompt([
//     {
//         label: 'First Name',
//         fieldname: 'first_name',
//         fieldtype: 'Data'
//     },
//     {
//         label: 'Last Name',
//         fieldname: 'last_name',
//         fieldtype: 'Data'
//     },
// ], (values) => {
//     console.log(values.first_name, values.last_name);
// })
//     }
// })

// frappe.confirm('Are you sure you want to proceed?',
//     () => {
//         frappe.msgprint("You selected Yes");
//     }, () => {
//         frappe.msgprint("You selected No");
//     })


// frappe.show_progress('Loading..',  110, 1000, 'Please wait');

//Check the path or the route of the document
// frappe.ui.form.on("Cus_1",{
//     refresh(frm){
//         let route = frappe.get_route();
//         console.log(route[0]);
//         console.log(route[1]);
//         console.log(route[2]);
//     }
// })


//Helps to create a own route and helps in navigation.

// frappe.ui.form.on("Cus_1", {
//     refresh(frm) {
//         frm.add_custom_button("Open Document", () => {
//             frappe.set_route("Form", "Cus_1", "nn0c525eom");
//         });
//     }
// });

frappe.call('ping').then(r => {
    console.log(r.message); // {message: "pong"}
});