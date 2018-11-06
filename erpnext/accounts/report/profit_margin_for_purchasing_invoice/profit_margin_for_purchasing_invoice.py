# Copyright (c) 2013, Revaluesoft S.A.E and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	data = get_data()
#	frappe.msgprint("LUAY")
	columns = get_columns()
	return columns , data

def get_data():
	accounts = frappe.db.sql("""SELECT
  `tabPurchase Invoice Item`.parenttype as "Type:Purchase Invoice:120",
  `tabPurchase Invoice Item`.parent as "Purchase Invoice:Link/Purchase Invoice:120",
  `tabItem Price`.currency as "Currency",
  `tabPurchase Invoice Item`.item_code as "Item Code:Link/Item:120",
  `tabPurchase Invoice Item`.description as "Description",
  `tabPurchase Invoice Item`.UOM as "uom",
  `tabPurchase Invoice Item`.Qty as "qty",
  `tabPurchase Invoice Item`.Rate as "rate",
  `tabItem Price`.price_list as "Price List",
  `tabItem Price`.price_list_rate as "Price List Rate",
  `tabPurchase Invoice Item`.valuation_rate as "valuation Rate",
  ( `tabPurchase Invoice Item`.valuation_rate * `tabPurchase Invoice Item`.qty ) as "Total Cost:Currency/Total Cost:100",
  ( `tabItem Price`.price_list_rate * `tabPurchase Invoice Item`.qty ) as "Total Revenue:Currency/Total Revenue:100",
  (( `tabItem Price`.price_list_rate * `tabPurchase Invoice Item`.qty) - (`tabPurchase Invoice Item`.valuation_rate * `tabPurchase Invoice Item`.qty)) as "Total Profit:Currency/Total Profit :100",
  Round ( ( ( `tabItem Price`.price_list_rate * `tabPurchase Invoice Item`.qty ) /  ( `tabPurchase Invoice Item`.valuation_rate * `tabPurchase Invoice Item`.qty )  * 100) , 2) as "Profit Margin:Percent/Profit Margin:100"
  FROM `tabPurchase Invoice Item`
  INNER JOIN `tabItem Price`
    ON `tabPurchase Invoice Item`.item_code = `tabItem Price`.item_code
  WHERE `tabItem Price`.selling = 1
  ORDER BY `tabPurchase Invoice Item`.parenttype, `tabPurchase Invoice Item`.parent""",debug=False)
		
	return accounts
	
def get_columns():
	return [
		{
			"fieldname": "parenttype",
			"label": ("Type"),
			"fieldtype": "Data",
			"options": "parenttype",
			"width": 120
		},
		{
			"fieldname": "parent",
			"label": ("Purchase Invoice"),
			"fieldtype": "Link",
			"options": "Purchase Invoice",
			"width": 120
		},
		{
			"fieldname": "currency",
			"label": ("Currency"),
			"fieldtype": "Data",
			"options": "Currency",
			"width": 120
		},
		{
			"fieldname": "item_code",
			"label": ("Item Code"),
			"fieldtype": "Link",
			"options": "Item",
			"width": 120
		},
		{
			"fieldname": "description",
			"label": ("Description"),
			"fieldtype": "Data",
			"options": "description",
			"width": 120
		},
		{
			"fieldname": "uom",
			"label": ("UOM"),
			"fieldtype": "Link",
			"options": "UOM",
			"width": 120
		},
		{
			"fieldname": "qty",
			"label": ("Qty"),
			"fieldtype": "Data",
			"options": "qty",
			"width": 120
		},
		{
			"fieldname": "rate",
			"label": ("Rate"),
			"fieldtype": "Data",
			"options": "rate",
			"width": 100
		},
		{
			"fieldname": "price_list",
			"label": ("Price List"),
			"fieldtype": "Link",
			"options": "Price List",
			"width": 100
		},
		{
			"fieldname": "price_list_rate",
			"label": ("Price List Rate"),
			"fieldtype": "Data",
			"options": "price_list_rate",
			"width": 100
		},
		{
			"fieldname": "valuation_rate",
			"label": ("Valuation Rate"),
			"fieldtype": "Data",
			"options": "valuation_rate",
			"width": 100
		},
		{
			"fieldname": "total_cost",
			"label": ("Total Cost"),
			"fieldtype": "Data",
			"options": "Total Cost",
			"width": 100
		},
		{
			"fieldname": "Tttal_revenue",
			"label": ("Total Revenue"),
			"fieldtype": "Data",
			"options": "Total Revenue",
			"width": 100
		},
		{
			"fieldname": "total_profit",
			"label": ("Total Profit"),
			"fieldtype": "Data",
			"options": "Total Profit",
			"width": 100
		},
		{
			"fieldname": "Profit_Margin",
			"label": ("Profit Margin"),
			"fieldtype": "Percent",
			"options": "Profit_Margin",
			"width": 100
		}
	]