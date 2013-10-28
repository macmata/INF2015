# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class RebateRule(Rule):
    PRIORITY = 4

    def rule_ordre_ingenieur(self):
        if self.quote.driver.oiq_member:
            self.quote.amount = int(self.quote.amount * 0.9)
