# Copyright (c) 2015, Revaluesoft S.A.E

from __future__ import unicode_literals
import frappe

def execute():
	frappe.db.set_value("DocType", "Maintenance Schedule", "module", "Maintenance")
	frappe.db.set_value("DocType", "Maintenance Schedule Detail", "module", "Maintenance")
	frappe.db.set_value("DocType", "Maintenance Schedule Item", "module", "Maintenance")
	frappe.db.set_value("DocType", "Maintenance Visit", "module", "Maintenance")
	frappe.db.set_value("DocType", "Maintenance Visit Purpose", "module", "Maintenance")