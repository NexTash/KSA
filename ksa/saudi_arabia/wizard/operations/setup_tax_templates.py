import json
import os
import frappe
from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data, simple_to_detailed

from ksa.saudi_arabia.setup import create_company_settings

@frappe.whitelist()
def create_vat_for_company(name):
    company = frappe.get_doc("Company", name)
    setup_templates(company)
    create_company_settings(company)


def setup_templates(doc,method=None):
	if doc.country == 'Saudi Arabia':
		file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ksa_template.json")
		with open(file_path, "r") as json_file:
			template = simple_to_detailed(json.load(json_file))
			from_detailed_data(doc.name,template)
			


