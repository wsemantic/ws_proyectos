from odoo import models, fields

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class XEncargo(models.Model):
    _name = 'x_encargo'
    _description = 'Encargo'

    nombre = fields.Char(string='Nombre')

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Relación múltiple a encargos
    encargos_ids = fields.Many2many(
        'x_encargo', 
        string='Encargos'
    )

    # Relación múltiple a productos
    producto_ids = fields.Many2many(
        'product.product', 
        string='Productos'
    )

    # Campo de tipo selección para el área de negocio
    area_negocio = fields.Selection(
        [
            ('department', 'Departmento'),
            ('tic', 'TIC'),
            ('innocamaras', 'Innocamaras'),
            ('tripartite', 'Tripartito'),
            ('idea', 'IDEA'),
            ('redes', 'Redes'),
            ('ecoinnocamaras', 'Ecoinnocamaras'),
            ('government', 'Gobierno'),
            ('without', 'Ninguna')        ,    

            # Añade más opciones según sea necesario
        ],
        string='Área de Negocio'
    )
