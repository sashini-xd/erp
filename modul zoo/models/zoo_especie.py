from odoo import models, fields
class zoo_especie(models.Model):
    _name = 'zoo.especie'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    perill = fields.Boolean('Perill de exincion (1 = si,0 = no)', required=True)
    familia = fields.Char('Familia')
    nomCientific = fields.Char('Nom cientific')
    nomVulgar = fields.Char('Nom vulgar')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognom)