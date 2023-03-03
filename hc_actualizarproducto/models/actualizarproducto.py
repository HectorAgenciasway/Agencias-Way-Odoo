from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round
from datetime import datetime

class Stock(models.Model):
    _inherit = 'product.template'
    
    def action_actualizarproducto(self):
        product = self

        producto_id = product.id

        mensaje = producto_id
        
        raise ValidationError(mensaje)