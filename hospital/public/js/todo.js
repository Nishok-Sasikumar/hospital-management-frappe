frappe.ui.form.on("ToDo", {
    refresh: function(frm) {
        frm.trigger("my_custom_code");
    },
    my_custom_code: function(frm) {
        console.log("ToDo name:", frm.doc.name);
        frm.dashboard.set_headline_alert("This ToDo was extended by the hospital app!");
    }
});