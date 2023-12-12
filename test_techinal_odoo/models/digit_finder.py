from odoo import models, fields, api

class DigitFinder(models.Model):
    _name = 'digit.finder'
    _description = 'Digit Finder'

    input_number = fields.Integer(string='Input Number', required=True)
    input_place = fields.Integer(string='Place (Index)', required=True)
    digit_at_place = fields.Integer(string='Digit at Place', compute='_compute_digit_at_place')
    digit_count = fields.Integer(string='Total Digits', compute='_compute_digit_count')

    @api.depends('input_number', 'input_place')
    def _compute_digit_at_place(self):
        for record in self:
            str_number = str(record.input_number)
            digit_count = len(str_number)
            if 0 <= record.input_place < digit_count:
                record.digit_at_place = int(str_number[record.input_place])
            else:
                record.digit_at_place = None

    @api.depends('input_number')
    def _compute_digit_count(self):
        for record in self:
            str_number = str(record.input_number)
            record.digit_count = len(str_number)