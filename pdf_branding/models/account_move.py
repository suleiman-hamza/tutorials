# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    def _default_brand_id(self):
        company = self.env.company
        return self.env["hunterr.brand"].search([("company_id", "=", company.id)], limit=1)

    brand_id = fields.Many2one(
        "hunterr.brand",
        string="Brand",
        domain="[('company_id', '=', company_id)]",
        default=_default_brand_id,
        help="Brand to use for PDF layout (header/footer).",
    )