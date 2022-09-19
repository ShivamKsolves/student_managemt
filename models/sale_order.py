from odoo import api, fields, models, _, tools


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Char(string='Test field')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    Total_Weight = fields.Float(string='Total Weight')
    # Tax_discount=fields.Float(string='Discounted Tax')
