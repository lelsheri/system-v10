# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

import frappe
import frappe.permissions

def execute():
	if "opn_description" in frappe.db.get_table_columns("BOM Operation"):
		frappe.db.sql("""update `tabBOM Operation` set description = opn_description 
			where ifnull(description, '') = ''""")