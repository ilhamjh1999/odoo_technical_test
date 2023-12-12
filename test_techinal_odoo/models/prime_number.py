from odoo import models, fields, api

class PrimeNumber(models.Model):
    _name = 'prime.number'
    _description = 'Prime Number Calculator'

    input_number = fields.Integer(string='Input Number', required=True)
    output_primes = fields.Text(string='Output Primes', compute='_compute_output_primes')

    @api.depends('input_number')
    def _compute_output_primes(self):
        for record in self:
            primes = record._get_primes_smaller_than_n(record.input_number)
            record.output_primes = ", ".join(map(str, primes))

    def _get_primes_smaller_than_n(self, n):
        primes = []
        for num in range(2, n):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes        
