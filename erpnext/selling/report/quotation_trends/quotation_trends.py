# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from erpnext.controllers.trends	import get_columns, get_data

def execute(filters=None):
	if not filters: filters ={}
	data = []
	conditions = get_columns(filters, "Quotation")
	data = get_data(filters, conditions)

	return conditions["columns"], data 