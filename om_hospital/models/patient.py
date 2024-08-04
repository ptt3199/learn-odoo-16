from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"  
    _inherit = ['mail.thread']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string='Is a Child?', tracking=True)
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', readonly=False)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError('Age must be recorded')

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ""

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10: 
            self.is_child = True
        else:
            self.is_child = False