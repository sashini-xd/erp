from odoo import models, fields
class plane_pilot(models.Model):
    _name = 'plane.pilot'
    name = fields.Char(compute='_get_name',string="Nom complet",readonly='True',store=False)
    nom = fields.Char('Nom', required=True)
    cognoms = fields.Char('Cognoms', required=True)
    nif = fields.Char('NIF', required=True)
    telf = fields.Char('Telfon', required=True)
    email = fields.Char('Email')

    def _get_name(self):
        for record in self:
            record.name = str(record.nom) + " " + str(record.cognom)