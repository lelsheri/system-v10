# Copyright (c) 2015, Revaluesoft S.A.E
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals

test_dependencies = ["Employee"]

import frappe
test_records = frappe.get_test_records('Sales Person')