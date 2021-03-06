# -*- coding: utf-8 -*-

import logging
from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder.rules import decorators
from builder.rules.vehicules import Cars, Motos, Car, Moto


class Allowed(Rule):
    PRIORITY = 0

    def create_vehicule(self):
        return (
            self.quote.vehicule.year,
            self.quote.vehicule.make,
            self.quote.vehicule.model
        )


    @decorators.moto
    def rule_vehicule_exists_moto(self):
        vehicule = self.create_vehicule()
        if vehicule in Motos:
            self.quote.vehicule.value = Motos[vehicule][1]
            self.quote.vehicule.cc = Motos[vehicule][0]
        else:
            logging.debug(
                "Not allowed, vehicule %s %s %s not in list" % vehicule
            )
            raise NotAllowed()


    @decorators.car
    def rule_vehicule_exists_car(self):
        vehicule = self.create_vehicule()
        if vehicule in Cars:
            self.quote.vehicule.value = Cars[vehicule]
        else:
            logging.debug(
                "Not allowed, vehicule %s %s %s not in list" % vehicule
            )
            raise NotAllowed()

    def rule_lives_quebec(self):
        if not self.quote.driver.province == u'Québec':
            logging.debug("Not allowed, driver not from Quebec")
            raise NotAllowed()

    def rule_vehicule_more_than_million(self):
        if self.quote.vehicule.value >= 1000000:
            if not (self.quote.vehicule.alarm and \
                self.quote.vehicule.interior_garage ):
                logging.debug("Not allowed, vehicule need \
                       a alarm and a interior garage")
                raise NotAllowed()

    @decorators.younger_than(25)
    @decorators.man
    def rule_25_man(self):
        logging.debug("Not allowed, man younger than 25")
        raise NotAllowed()

    @decorators.younger_than(21)
    @decorators.woman
    def rule_21_woman(self):
        logging.debug("Not allowed, woman younger than 21")
        raise NotAllowed()

    @decorators.older_than(75)
    def rule_older_75(self):
        logging.debug("Not allowed, older than 75")
        raise NotAllowed()
