# -*- coding: utf-8 -*-

import logging

from builder.rules import Rule
from builder.rules import decorators


class RebateRule(Rule):
    PRIORITY = 4

    
    def rule_ordre_ingenieur(self):
        if self.quote.driver.oiq_member:
            logging.debug("OIQ member, applying 10% rebate")
            self.quote.amount = self.quote.amount * 0.9


    @decorators.braket_date(11,1,11,15)
    def rule_starting_10(self):
        logging.debug("Contract starts between 1 and 15 of novembre")
        self.quote.amount = self.quote.amount * 0.90

    @decorators.braket_date(2,14,3,3)
    def rule_starting_5(self):
        logging.debug("Contract starts between 14 feb to 3 mars")
        self.quote.amount = self.quote.amount * 0.95
