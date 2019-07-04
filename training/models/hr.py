# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    job_category = fields.Selection(string="Job category", selection=[('driver', 'Driver'), ('teacher', 'Teacher'), ],
                                    required=False,) ## required se ne mora definirati, jer je po defaultu False
    training_ids = fields.One2many("training.training", 'trainer_id', string="Trainings", required=False, )








