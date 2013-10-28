# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class GeneralRules(Rule):
    PRIORITY = 3

    @decorators.moto
    def rule_moto_1000cc(self):
        if self.quote.vehicule.cc > 1000:
            self.quote.amount += 100000

    def rule_vehicule_plus_500000(self):
        if self.quote.vehicule.value > 500000:
            self.quote.amount += 250000

    def rule_options(self):
        self.quote.amount += \
            int((self.quote.vehicule.option_value * 100) * 0.10)

    def rule_lives_in(self):
        if self.quote.driver.city in (u'Longueuil', u'Montréal'):
            self.quote.amount += 20000

    def rule_sherlock(self):
        if self.quote.vehicule.chiseling == 'Sherlock':
            self.quote.amount -= 25000

    def rule_interior_garage(self):
        if self.quote.vehicule.interior_garage:
            self.quote.amount -= 50000

    def rule_alarm_system(self):
        if self.quote.vehicule.alarm:
            self.quote.amount -= 50000

    def rule_cours_conduite_caa(self):
        if self.quote.driver.driving_lessons_caa:
            self.quote.amount -= 10000

    def rule_premier_contrat(self):
        if self.quote.driver.first_contract:
            self.quote.amount += 200000

    def rule_annee_experience(self):
        if self.quote.driver.years_experience > 15:
            self.quote.amount -= 40000

