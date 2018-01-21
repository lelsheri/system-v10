# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.reload_doctype("Stock Entry")
	frappe.db.sql("update `tabStock Entry` set from_bom = if(ifnull(bom_no, '')='', 0, 1)")
