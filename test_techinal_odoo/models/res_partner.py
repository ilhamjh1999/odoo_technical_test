from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Inherit Res Partner'

    supplier = fields.Boolean(string='Is a Supplier', default=False)
   

   
