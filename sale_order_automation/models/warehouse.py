from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    x_is_delivery_set_to_done = fields.Boolean(string="Is Delivery Set to Done")
    x_create_invoice=fields.Boolean(string='Create Invoice?')
    x_validate_invoice = fields.Boolean(string='Validate invoice?')