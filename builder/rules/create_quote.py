# -*- coding: utf-8 -*-

import logging

from builder.rules import Rule, decorators


class CreateQuote(Rule):
    PRIORITY = 1

    @decorators.woman
    @decorators.braket_age(21, 40)
    def rule_woman_21_50(self):
        logging.debug("Woman, 21 - 40")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.11)

    @decorators.woman
    @decorators.braket_age(41, 65)
    def rule_woman_41_65(self):
        logging.debug("Woman, 41 - 65")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.9)

    @decorators.woman
    @decorators.braket_age(66, 75)
    def rule_woman_66_75(self):
        logging.debug("Woman, 66 - 75")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.155)

    @decorators.man
    @decorators.braket_age(25, 35)
    def rule_man_25_35(self):
        logging.debug("Man, 21 - 50")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.15)

    @decorators.man
    @decorators.braket_age(36, 60)
    def rule_man_36_60(self):
        logging.debug("Man, 36 - 60")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.12)

    @decorators.man
    @decorators.braket_age(61, 75)
    def rule_man_61_75(self):
        logging.debug("Man, 61 - 75")
        self.quote.montant = int(self.quote.vehicule.value * 100 * 0.135)
        self.quote.montant *= 1.135
