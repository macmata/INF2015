# -*- coding: utf-8 -*-

import logging
from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder.rules import decorators
from builder.rules.vehicules import Cars, Motos
from builder.quote import Car, Moto


class Allowed(Rule):
    PRIORITY = 0

    def rule_vehicule_exists(self):
        vehicule = (
            self.quote.vehicule.annee,
            self.quote.vehicule.marque,
            self.quote.vehicule.modele
        )
        #pdb.set_trace()
        if isinstance(self.quote.vehicule, Car) and vehicule in Cars:
            self.quote.car.value = Cars[vehicule]
            self.quote.car.valueInit = Cars[vehicule]
        elif isinstance(self.quote.vehicule, Moto) and vehicule in Motos:
            self.quote.car.value = Motos[vehicule]
            self.quote.car.valueInit = Motos[vehicule]
        else:
            logging.debug("Not allowed, car not in list")
            raise NotAllowed()

    def rule_lives_quebec(self):
        if not self.quote.driver.province == 'Québec':
            logging.debug("Not allowed, driver not from Quebec")
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
    def rule_genraise(self):
        logging.debug("Not allowed, older than 75")
        raise NotAllowed()
