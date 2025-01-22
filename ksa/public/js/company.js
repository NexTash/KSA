frappe.provide("erpnext.company");

frappe.ui.form.on("Company", {
  refresh(frm) {
    frm.add_custom_button("Create VAT Settings", () => {
      frappe.call({
        method:
          "ksa.saudi_arabia.wizard.operations.setup_tax_templates.create_vat_for_company",
        args: {
          name: frm.doc.name,
        },
        freeze: true,
        callback: function (r) {
          if (r) {
          }
        },
      });
    });
  },
});
