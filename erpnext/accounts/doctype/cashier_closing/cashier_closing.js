// Copyright (c) 2018, Revaluesoft S.A.E and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cashier Closing', {

	setup: function(frm){
		if (frm.doc.user == "" || frm.doc.user == null) {
			frm.doc.user = frappe.session.user;
		}
	}
});
