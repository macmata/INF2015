# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class RebateRule(Rule):
    PRIORITY = 4

    def rule_ordre_ingenieur(self):
        if self.quote.driver.membre_oiq:
            self.quote.montant = int(self.quote.montant * 0.9)
