# Copyright (c) 2015, Revaluesoft S.A.E and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class Operation(Document):
	def validate(self):
		if not self.description:
			self.description = self.name
