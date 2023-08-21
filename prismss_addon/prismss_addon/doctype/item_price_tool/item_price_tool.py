# Copyright (c) 2023, InshaSiS Techonologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ItemPriceTool(Document):
	def on_submit(self):
		for i in self.item_price_tool_table:
			item_price_tool = frappe.new_doc("Item Price")
			item_price_tool.item_code = self.item_code
			item_price_tool.price_list = i.item_price
			item_price_tool.selling = 1
			item_price_tool.price_list_rate = i.rate
			item_price_tool.save(ignore_permissions=True)

		frappe.msgprint("Item Price Create Successfully!")
