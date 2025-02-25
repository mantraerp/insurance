// Copyright (c) 2025, Mantra and contributors
// For license information, please see license.txt

frappe.ui.form.on('Policy', {
    period_to: function(frm) {
        if (frm.doc.period_from && frm.doc.period_to) {

            let period_from = frappe.datetime.str_to_user(frm.doc.period_from);
            let period_to = frappe.datetime.str_to_user(frm.doc.period_to);

            if (period_to <= period_from) {
                frappe.throw(`End Date (${period_to}) must be later than Start Date (${period_from})`);
            }
        }
    }
});
