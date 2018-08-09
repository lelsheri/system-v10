// Copyright (c) 2018, Revaluesoft S.A.E and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cashier Closing', {

	expense: function(frm){
		frm.doc.net_amount = frm.doc.expense + frm.doc.in_save - frm.doc.custody;
	},

	custody: function(frm){
		frm.doc.net_amount = frm.doc.expense + frm.doc.in_save - frm.doc.custody;
	},

	in_save: function(frm){
		frm.doc.user = frappe.session.user;
		frm.doc.net_amount = frm.doc.expense + frm.doc.in_save - frm.doc.custody;
	}
});
