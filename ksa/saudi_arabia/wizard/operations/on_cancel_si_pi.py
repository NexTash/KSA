import frappe
def prevent_cancel_if_qr(doc, method):
   
    """
    Prevent cancelation if `ksa_einv_qr` field exists in the document.
    """
    if doc.get('ksa_einv_qr'):
        frappe.throw(
            ("This document cannot be canceled or edited as per ZATCA compliance. This invoice must be submitted to the ZATCA authority")
        )