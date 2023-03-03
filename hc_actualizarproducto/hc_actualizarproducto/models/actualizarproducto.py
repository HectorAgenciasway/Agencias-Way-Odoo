from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_round
from datetime import datetime
import json, requests

class Stock(models.Model):
    _inherit = 'product.template'
   
    def action_actualizar_producto(self):
        product = self
        

        producto_id = product.id
       #nombre = product.name
        
     """sku = product.id
        name = product.name
        descripcion = product.x_studio_modelo
        categoria = product.categ_id.id ##validar
        tangibilidad = product.detailed_type
        comercializacion = product.x_studio_regalia
        upc = "0"
        precio = product.list_price
        fotografia = product.image_512
        extension = "png"
        
        id_marca= product.x_studio_related_field_z0kT7
        id_linea=datos = product.x_studio_codigo_linea
        id_grupo=datos = product.x_studio_codigo_grupo_1
        
       ## marca=models.execute_kw(db, uid, password, 'x_nombre_marca', 'search_read', [[["x_studio_codigo_marca_1", "=", id_marca]]],{'fields':["x_studio_nombre_principal"]})

        ##nombre_marca_arr = marca[0]

        ##nombre_marca = nombre_marca_arr["x_studio_nombre_principal"]
        
    
        
        if fotografia == False:
          fotografia = "0"
            
        
        url_api_way = "http://143.198.49.228:8080/API_WS_PROCESOS_WAY/webresources/Creacion_Producto"
        
        r = {
            'sku':sku,
            'nombre':name,
            'descripcion':descripcion,
            'marca_producto':id_marca,
            'linea_producto':id_linea,
            'grupo_producto':id_grupo,
            'categoria_producto':categoria,
            'tangibilidadId':tangibilidad,
            'comercializacionId':comercializacion,
            'upc':upc,
            'precio':precio,
            'fotografia':"0",
            'extension':extension,
        }
        
        cabeceras = {'correo': 'devcom', 'password': 'Way2023'} 

        response = requests.post(url_api_way, data=json.dumps(r), headers=cabeceras)
        
        response_json = response.json()

        id_error = response_json['id_error']
        
        descripcion_error = response_json["descripcion_error"]
        
        informacion_error =  response_json["informacion_error"]"""
        
        mensaje = producto_id

        ##mensaje = producto_id
        ##mensaje2 = nombre
        ##conca = mensaje," ", mensaje2," "
        
        
        raise ValidationError(mensaje)
        