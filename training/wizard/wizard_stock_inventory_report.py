# -*- encoding: utf-8 -*-
from odoo import api, models, fields


class TrainingReportWizad(models.TransientModel):
    _name = 'training.report.wizard'
    _description = 'Wizard that opens the form for printing training reports'

    trainer_id = fields.Many2one('hr.employee', 'Trainer', required=True)
    date_from = fields.Date('Date from')
    date_to = fields.Date('Date to')


    @api.multi
    def print_report(self):
        self.ensure_one()
        data = {'ids': self.env.context.get('active_ids', [])}
        res = self.read()
        res = res and res[0] or {}
        data.update({'form': res})
        return self.env['report'].get_action(self, 'training.report_training_list', data=data)
