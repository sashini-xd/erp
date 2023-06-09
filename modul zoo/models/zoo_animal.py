from odoo import models, fields
class zoo_animal(models.Model):
    _name = 'zoo.animal'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    continentOrigen = fields.Char('Continent de origen', required=True)
    dataNaix = fields.Date('Data de naixament')
    paisOrigen = fields.Char('Ciutat')
    sexe = fields.Char('sexe')

    
    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognom)