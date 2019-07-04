# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class trainingLocation(models.Model):
    _name = 'location.training'

    name = fields.Char('Name', limit=20, required=True)
    adress = fields.Char('Adress', limit=20)
    city = fields.Char('City')
    country = fields.Many2one('res.country',string = 'Country')
    description = fields.Html('Description')
    addition = fields.Text('Practice!')
    training_ids = fields.One2many('training.training', 'location_id', 'Trainings' , readonly=True)
    active = fields.Boolean('Active', default=True)


