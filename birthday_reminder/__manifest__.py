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

{
    'name': "Birthday Reminder",
    'description': """
        Long description of module's purpose
    """,
    'author': "Uvid",
    'website': "https://odoo.com.hr/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['hr'],
    'data': [
        'views/hr.xml',
        'views/birthday.xml',
        'report/report_birthday.xml',
        'data/cron.xml',
    ],
    'installable': True,
}