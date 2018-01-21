# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.db.sql("""Update `tabAccount` set account_type = 'Temporary' 
		where account_name in ('Temporary Assets', 'Temporary Liabilities', 'Temporary Opening')""")