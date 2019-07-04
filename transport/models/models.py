# -*- coding: utf-8 -*-

from odoo import models, fields, api


class transport(models.Model):
    _name = 'transporter.transport'

    name = fields.Char('Name', limit=20, required=True)
    type = fields.Char('Type', limit=20)
    model = fields.Char('Model', limit=20)
    year = fields.Integer('Year')
    fuel = fields.Float('Fuel consumption /100km')
    description = fields.Text('Description')
    color = fields.Char('Color')
    about = fields.Text('About')
    travels_ids = fields.One2many('relations.transport', 'correct_id', 'Travels')


class relations(models.Model):
    _name = 'relations.transport'

    correct_id = fields.Many2one('transporter.transport', 'correct_id')
    start_city = fields.Char('Start', limit=20, required=True)
    end_city = fields.Char('End', limit=20, required=True)
    distance = fields.Float('Distance')
    time_travel = fields.Float('Time travel')


    @api.multi
    def name_get(self):
        res = []
        for record in self:
            #import pdb; pdb.set_trace()
            name = record.start_city + '-' + record.end_city
            if record.distance:
                name += ' ' + str(record.distance)
            res.append((record.id,name))
        return res



class travel(models.Model):
    _name = 'travels.transport'

    name = fields.Char('Travel name')
    date = fields.Date('Date')
    car_id = fields.Many2one('transporter.transport','Car')
    relation_id = fields.Many2one('relations.transport','Relation')
    fuel_over = fields.Float('Fuel consumption', readonly=True, compute ='_consumption_sum')
    travel_time = fields.Float('relation_id.time_travel',readonly=True)
    add = fields.Float(related='car_id.fuel',readonly=True)
    add_1 = fields.Float(related='relation_id.distance',readonly=True)



    @api.depends('car_id.fuel', 'relation_id.distance')
    def _consumption_sum(self):
        for travels in self:
            # import pdb;pdb.set_trace()
            travels.fuel_over = travels.add*(travels.add_1/100)


