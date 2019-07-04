# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from dateutil import parser
from datetime import timedelta

class trainingTraining(models.Model):
    _name = 'training.training'

    def _get_default_employee(self):
        empObj = self.env['hr.employee']
        employee = empObj.search([('user_id', '=', self.env.user.id)], limit=1)
        if employee:
            return employee

    name = fields.Char('Name', limit=20, required=True)
    description = fields.Text('Description')
    length_days = fields.Integer('Length In Days', default=2)
    start_date = fields.Date('Start Date', default=fields.Date.today)
    end_date = fields.Date('End Date')
    price = fields.Float('Training Price', digits=(16, 4))
    # create_date = fields.Datetime('Created On', readonly=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')], default='draft')
    student_ids = fields.One2many('training.student', 'training_id', 'Students')
    trainer_id = fields.Many2one('hr.employee', 'Trainer', required=True, default=_get_default_employee)
    number = fields.Char('Number', readonly=True)
    location_id = fields.Many2one('location.training', 'Location')
    hall_ids = fields.Many2many('training.hall', string='Halls')
    # hall2_ids = fields.Many2many('training.hall', 'traings_to_hall_rel', 'training_id', 'hall_id', string='Halls')
    color = fields.Integer('Color')
    trainer_country_id = fields.Many2one('res.country', related='trainer_id.country_id',
                                         string='Trainer Country', readonly=True)
    trainer_currency_symbol = fields.Char('Trainer Currency Code', related='trainer_id.country_id.currency_id.symbol', readonly=True)
    trainer_currency_symbol_depends = fields.Char('Trainer Currency Code Depends', compute='_compute_symbol', readonly=True, store=True)
    total_amount = fields.Float('Total Amount', compute='_compute_total_amount', digits=(16, 4), readonly=True, store=True)

    _sql_constraints = [
        ('number_uniq', 'unique(number)', 'Training Number must be unique!'),
    ]

    @api.constrains('price')
    def _check_price(self):
        for training in self:
            if training.price > 10000:
                raise UserError(_('Maximum price of 10000 excedeed!'))

    @api.depends('price', 'student_ids')
    def _compute_total_amount(self):
        for training in self:
            training.total_amount = training.price * len(training.student_ids)

    @api.depends('trainer_id', 'trainer_id.country_id', 'trainer_id.country_id.currency_id', 'trainer_id.country_id.currency_id.symbol')
    def _compute_symbol(self):
        for training in self:
            training.trainer_currency_symbol_depends = training.trainer_id.country_id.currency_id.symbol

    @api.multi
    @api.onchange('length_days')
    def change_length_days(self):
        if self.start_date and self.length_days:
            self.end_date = parser.parse(self.start_date) + timedelta(days=self.length_days)
        else:
            self.end_date = False

    @api.multi
    @api.onchange('start_date')
    def change_start_date(self):
        if self.start_date and self.length_days:
            self.end_date = parser.parse(self.start_date) + timedelta(days=self.length_days)
        else:
            self.end_date = False

    @api.multi
    @api.onchange('end_date')
    def change_end_date(self):
        if self.end_date and self.length_days:
            self.start_date = parser.parse(self.end_date) - timedelta(days=self.length_days)
        else:
            self.start_date = False

    @api.multi
    def action_confirm(self):
        for training in self:
            training.state = 'confirmed'

    @api.multi
    def action_done(self):
        for training in self:
            training.state = 'done'

    @api.multi
    def action_cancel(self):
        for training in self:
            training.state = 'cancel'

    @api.multi
    def action_activate(self):
        for training in self:
            training.state = 'draft'

    @api.model
    def create(self, vals):
        vals['number'] = self.env['ir.sequence'].next_by_code('training') or _('NaV')

        res = super(trainingTraining, self).create(vals)

        return res

    @api.multi
    def unlink(self):
        # for training in self:
        #     if training.state != 'cancel':
        #         raise UserError(_('You cannot delete training that are not canceled!'))

        if self.filtered(lambda x: x.state not in ('cancel')):
            raise UserError(_('You cannot delete training that are not canceled!'))

        return super(trainingTraining, self).unlink()

class studentTraining(models.Model):
    _name = 'training.student'

    training_id = fields.Many2one('training.training', 'Training', required=True, readonly=True)
    name = fields.Char('Name', limit=20, required=True)
    surname = fields.Char('Surname', limit=30)
    age = fields.Integer('Age')


class hallTraining(models.Model):
    _name = 'training.hall'

    name = fields.Char('Name', limit=20, required=True)
