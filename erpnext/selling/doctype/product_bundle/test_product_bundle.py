
# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals


import frappe
test_records = frappe.get_test_records('Product Bundle')

def make_product_bundle(parent, items):
	if frappe.db.exists("Product Bundle", parent):
		return frappe.get_doc("Product Bundle", parent)

	product_bundle = frappe.get_doc({
		"doctype": "Product Bundle",
		"new_item_code": parent
	})

	for item in items:
		product_bundle.append("items", {"item_code": item, "qty": 1})

	product_bundle.insert()

	return product_bundle
