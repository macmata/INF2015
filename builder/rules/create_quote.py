# -*- coding: utf-8 -*-

import logging

from builder.rules import Rule, decorators


class CreateQuote(Rule):
    PRIORITY = 2

    @decorators.car
    @decorators.woman
    @decorators.bracket_age(21, 40)
    def rule_woman_21_50_car(self):
        logging.debug("Car Woman, 21 - 40")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.11)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.car
    @decorators.woman
    @decorators.bracket_age(41, 65)
    def rule_woman_41_65_car(self):
        logging.debug("Car Woman, 41 - 65")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.09)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.car
    @decorators.woman
    @decorators.bracket_age(66, 75)
    def rule_woman_66_75_car(self):
        logging.debug("Car Woman, 66 - 75")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.155)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.car
    @decorators.man
    @decorators.bracket_age(25, 35)
    def rule_man_25_35_car(self):
        logging.debug("Car Man, 25 - 35")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.15)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.car
    @decorators.man
    @decorators.bracket_age(36, 60)
    def rule_man_36_60_car(self):
        logging.debug("Car Man, 36 - 60")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.12)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.car
    @decorators.man
    @decorators.bracket_age(61, 75)
    def rule_man_61_75_car(self):
        logging.debug("Car Man, 61 - 75")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.135)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.woman
    @decorators.bracket_age(21, 40)
    def rule_woman_21_50_moto(self):
        logging.debug("Moto Woman, 21 - 40")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.25)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.woman
    @decorators.bracket_age(41, 65)
    def rule_woman_41_65_moto(self):
        logging.debug("Moto Woman, 41 - 65")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.23)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.woman
    @decorators.bracket_age(66, 75)
    def rule_woman_66_75_moto(self):
        logging.debug("Moto Woman, 66 - 75")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.295)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.man
    @decorators.bracket_age(25, 35)
    def rule_man_25_35_moto(self):
        logging.debug("Moto Man, 25 - 35")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.29)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.man
    @decorators.bracket_age(36, 60)
    def rule_man_36_60_moto(self):
        logging.debug("Moto Man, 36 - 60")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.26)
        logging.debug("Quote starting amount: %d", self.quote.amount)

    @decorators.moto
    @decorators.man
    @decorators.bracket_age(61, 75)
    def rule_man_61_75_moto(self):
        logging.debug("Moto Man, 61 - 75")
        self.quote.amount = int(self.quote.vehicule.value * 100 * 0.275)
        logging.debug("Quote starting amount: %d", self.quote.amount)
