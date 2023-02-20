from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round
from datetime import datetime

class Stock(models.Model):
    _inherit = 'product.template'
    producto_id = self.id	
    
    def action_aw(self):

        mensaje = producto_id
		
        raise ValidationError(mensaje)