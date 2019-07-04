from odoo import models, fields, api, _
from datetime import datetime

class EmployeeBirthday(models.Model):
    _name = 'employee.birthday'

    def _get_this_month(self):
        today = datetime.now()
        month = str(today.month)
        return '0' + month if len(month) == 1 else month

    name = fields.Char('Name')
    month = fields.Selection([('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'),
                              ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'),
                              ('10', 'October'), ('11', 'November'), ('12', 'December')], default=_get_this_month)
    line_ids = fields.One2many('employee.birthday.line', 'birthday_id', 'Lines')
    ### onchange mjeseca puni u name mjesec/godina npr 03/2018
    ### napraviti novu klasu employee.birthday.lines koja ima polja
        #- employee_id many2one na hr.employee
        #- godine ingeter polje
        # - vezu na employee birtday
    ### napraviti one2many polje u employee.birthday klasi sa povezanim stavkama(
    ##employee.birthday.lines

    def get_employee(self):
        lines = []
        empObj = self.env['hr.employee']
        self.line_ids.unlink()
        employees = empObj.search([('month', '=', self.month)])
        for emp in employees:
            emp_lines = {
                'employee_id': emp.id,
                'birthday_id': self.id,
            }
            lines.append((0, 0, emp_lines))
        self.write({'line_ids': lines})

    @api.model
    def _send_report(self):
        import pdb;pdb.set_trace()


class EmployeeBirthdayLine(models.Model):
    _name = 'employee.birthday.line'

    employee_id = fields.Many2one('hr.employee', 'Employee')
    age = fields.Integer('Age') ### neka bude funkcijsko (compute) polje koje ce se
    #racunati svaki put kada udjemo u formu,
    # ne store-a se u bazu (trenutna godina-godina rodjenja)
    birthday_id = fields.Many2one('Birthday')
