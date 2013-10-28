# -*- coding: utf-8 -*-

import logging

from builder.rules import Rule
from builder.rules import decorators


class RebateRule(Rule):
    PRIORITY = 4

    def rule_ordre_ingenieur(self):
        if self.quote.driver.oiq_member:
            logging.debug("OIQ member, applying 10% rebate")
            self.quote.amount = int(self.quote.amount * 0.9)
