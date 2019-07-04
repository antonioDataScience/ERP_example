# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source ERP Solution
#    Author: Uvid d.o.o.
#    Copyright: Uvid d.o.o.
#    web: https://odoo.com.hr/
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


from odoo import models, fields, api, _
from datetime import datetime

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    day = fields.Integer('Day')
    month = fields.Integer('Month')

    @api.multi
    @api.onchange('birthday')
    def onchange_birthday(self):
        if self.birthday:
            birthday_dt = datetime.strptime(self.birthday, '%Y-%m-%d')
            self.day = birthday_dt.day
            self.month = birthday_dt.month




