# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.website.render

page_title = "Partners"

def get_context(context):
	partners = frappe.db.sql("""select * from `tabSales Partner`
			where show_in_website=1 order by name asc""", as_dict=True)

	return {
		"partners": partners,
		"title": page_title
	}
