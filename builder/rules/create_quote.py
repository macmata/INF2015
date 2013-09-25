# -*- coding: utf-8 -*-

from builder.rules import Rule


class CreateQuote(Rule):
    PRIORITY = 1

    def rule_create(self):
        print("execution regle 001")
        if not hasattr(self.quote.car, 'value'):
            raise Exception("Car value was not set")

        if self.quote.contrat.duree == 3:
            self.car.value *= 0.85
        self.quote.montant = self.quote.car.value * 0.09
