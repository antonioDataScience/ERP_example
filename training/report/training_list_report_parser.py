# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source ERP Solution
#    Author: Uvid d.o.o.
#    Copyright: Uvid d.o.o.
#    web: www.uvid.hr
#    e-mail: info@uvid.hr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from odoo import models, api
from odoo.exceptions import UserError

class ReportTrainingList(models.AbstractModel):
    _name = 'report.training.report_training_list'

    def _get_training(self, data):
        trainer = data['form'].get('trainer_id')[0]
        date_from = data['form'].get('date_from') or None
        date_to = data['form'].get('date_to') or None
        domain = [('trainer_id', '=', trainer)]
        if date_from:
            domain.append(('date_from', '>=', date_from))
        if date_to:
            domain.append(('date_to', '>=', date_to))
        trainings = self.env['training.training'].search(domain)
        ### ista stvar sa cistim sql
        sql = '''
            select 
              id 
            from 
              training_training
            where
              trainer_id = {0}
            '''.format(trainer)
        if date_from:
            sql += ''' and 'date_from' >= {}'''.format(date_from)
        if date_to:
            sql += ''' and 'date_to' <= {}'''.format(date_to)
        self.env.cr.execute(sql)
        trainings = self.env['training.training'].browse([line[0] for line in self.env.cr.fetchall()])
        #### Dobivam listu sa cistim ID-evima i odmah ih pretvaram u objekte i sibam dalje
        return trainings


    @api.model
    def render_html(self, docids, data=None):
        if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
            raise UserError(_("Form content is missing, this report cannot be printed."))
        ### Ako ne dobijemo form u data varijabli baci error, nuzno je da iz wizarda dobijemo podatke koje trebamo prikazati
        docs = self.env['training.report.wizard'].browse(self.env.context.get('active_id'))
        ### Ocekuje neki model nad kojem je napravljen model, prosljedjujem mu model wizarda koji se dize
        docargs = {
            'doc_ids': docids,
            'doc_model': 'training.report.wizard',
            'data': data,
            'docs': docs,
            'training_list': self._get_training(data)
        }
        ### neke defaultne vrijednosti koje ova metoda ocekuje, sa iznimkom training_list koja je nasa varijabla koja vraca listu
        ### treninga
        return self.env['report'].render('training.report_training_list', docargs)
        ### ovdje vracamo naziv reporta koji zovemo





