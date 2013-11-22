# -*- coding: utf-8 -*-

import logging

from builder.rules import Rule
from builder.rules import decorators


class GeneralRules(Rule):
    PRIORITY = 3

    @decorators.moto
    def rule_moto_1000cc(self):
        if self.quote.vehicule.cc > 1100:
            logging.debug("Moto cc > 1100")
            self.quote.amount += 100000

    def rule_vehicule_value_more_than_500000(self):
        if self.quote.vehicule.value > 500000:
            logging.debug("Vehicule's value is more than 500 000$")
            self.quote.amount += 250000

    def rule_options(self):
        value_to_add = (self.quote.vehicule.option_value * 100) * 0.10
        logging.debug("Adding option values (%.2f)$" % (value_to_add / 100))
        self.quote.amount += value_to_add

    def rule_lives_in(self):
        if self.quote.driver.city in (u'Longueuil', u'Montréal'):
            logging.debug("Driver lives in Longueuil or Montreal")
            self.quote.amount += 20000
        else:
            logging.debug("Driver lives OUTSIDE of Longueuil or Montreal")

    def rule_sherlock(self):
        if self.quote.vehicule.chiseling == 'Sherlock':
            logging.debug("Chiseling is from Sherlock")
            self.quote.amount -= 25000
        else:
            logging.debug("Chiseling is NOT from Sherlock")

    def rule_interior_garage(self):
        if self.quote.vehicule.interior_garage:
            logging.debug("Interior garage")
            self.quote.amount -= 50000
        else:
            logging.debug("NO interioir garage")

    def rule_alarm_system(self):
        if self.quote.vehicule.alarm:
            logging.debug("Vehicule has an alarm")
            self.quote.amount -= 50000
        else:
            logging.debug("NO alarm")

    def rule_driving_lessons_from_caa(self):
        if self.quote.driver.driving_lessons_caa:
            logging.debug("Driver has driving lessons from CAA")
            self.quote.amount -= 10000
        else:
            logging.debug("Driver NOT CAA")

    def rule_first_contract(self):
        if self.quote.driver.first_contract:
            logging.debug("First contract")
            self.quote.amount += 200000
        else:
            logging.debug("Driver NOT first contract")

    def rule_annee_experience(self):
        if self.quote.driver.years_experience >= 15:
            logging.debug("Driver has 15 years or more of experience")
            self.quote.amount -= 40000
        else:
            logging.debug("Driver NOT 15 years of experience")
