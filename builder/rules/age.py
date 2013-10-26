# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class GeneralRules(Rule):
    PRIORITY = 2

    @decorators.woman
    @decorators.braket_age(21, 50)
    def rule_woman_21_50(self):
        self.quote.montant *= 1.11

    @decorators.woman
    @decorators.braket_age(41, 65)
    def rule_woman_41_65(self):
        self.quote.montant *= 1.09

    @decorators.woman
    @decorators.braket_age(66, 75)
    def rule_woman_66_75(self):
        self.quote.montant *= 1.15

    @decorators.man
    @decorators.braket_age(25, 35)
    def rule_man_25_35(self):
        self.quote.montant *= 1.15

    @decorators.man
    @decorators.braket_age(36, 60)
    def rule_man_36_60(self):
        self.quote.montant *= 1.12

    @decorators.man
    @decorators.braket_age(61, 75)
    def rule_man_61_75(self):
        self.quote.montant *= 1.135
