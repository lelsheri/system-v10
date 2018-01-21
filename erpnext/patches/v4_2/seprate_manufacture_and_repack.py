# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.db.sql("""update `tabStock Entry` set purpose='Manufacture' where purpose='Manufacture/Repack' and ifnull(production_order,"")!="" """)
	frappe.db.sql("""update `tabStock Entry` set purpose='Repack' where purpose='Manufacture/Repack' and ifnull(production_order,"")="" """)