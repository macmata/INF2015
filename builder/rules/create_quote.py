# -*- coding: utf-8 -*-

from builder.rules import Rule


class CreateQuote(Rule):
    PRIORITY = 1

    def legacy_rule_create(self):
    	"""legacy rulefrom part 1"""
        if not hasattr(self.quote.car, 'value'):
            raise Exception("Car value was not set")

        if self.quote.contrat.duree == 3:
            self.quote.car.value *= 0.85
        self.quote.montant = int(self.quote.car.value * 0.09 * 100)

        if self.quote.car.valueInit > 500000:
            self.quote.montant += 250000
