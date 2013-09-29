import logging

from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder.rules import decorators

CARS = {}
CARS[(2014,"Porsche","Boxter")] = 60000
CARS[(2014,"Porsche","Boxter S")] = 72000
CARS[(2014,"Porsche","Cayman")] = 62000
CARS[(2014,"Porsche","Cayman S")] = 75000
CARS[(2014,"Porsche","911 Carrera")] = 100000
CARS[(2014,"Porsche","911 Carrera S")] = 115000
CARS[(2014,"Porsche","911 Carrera Cabriolet")] = 112000
CARS[(2014,"Porsche","911 Carrera S Cabriolet")] = 129000
CARS[(2014,"Porsche","911 Carrera 4")] = 106000
CARS[(2014,"Porsche","911 Carrera 4S")] = 123000
CARS[(2014,"Porsche","911 Carrera 4 Cabriolet")] = 120000
CARS[(2014,"Porsche","911 Carrera 4S Cabriolet")] = 137000
CARS[(2014,"Porsche","911 50 ans")] = 142000
CARS[(2014,"Porsche","911 Turbo")] = 170000
CARS[(2014,"Porsche","911 Turbo S")] = 207000
CARS[(2014,"Porsche","911 GT3")] = 149000
CARS[(2014,"Porsche","Panamera")] = 90000
CARS[(2014,"Porsche","Panamera 4")] = 95000
CARS[(2014,"Porsche","Panamera S")] = 107000
CARS[(2014,"Porsche","Panamera S E-Hybride")] = 114000
CARS[(2014,"Porsche","Panamera 4S")] = 113000
CARS[(2014,"Porsche","Panamera 4S Executive")] = 144000
CARS[(2014,"Porsche","Paramera GTS")] = 130000
CARS[(2014,"Porsche","Paramera Turbo")] = 162000
CARS[(2014,"Porsche","Paramera Turbo Executive")] = 185000
CARS[(2014,"Porsche","Cayenne")] = 59000
CARS[(2014,"Porsche","Cayenne Diesel")] = 67000
CARS[(2014,"Porsche","Cayenne S")] = 77000
CARS[(2014,"Porsche","Cayenne S Hybride")] = 82000
CARS[(2014,"Porsche","Cayenne GTS")] = 96000
CARS[(2014,"Porsche","Cayenne Turbo")] = 125000
CARS[(2014,"Porsche","Cayenne Turbo S")] = 169000


class Allowed(Rule):
    PRIORITY = 0

    def rule_car_allowed(self):
        car = (
            self.quote.car.annee,
            self.quote.car.marque,
            self.quote.car.modele
        )
        if car in CARS:
            self.quote.car.value = CARS[car]
        else:
            logging.debug("Not allowed, car not in list")
            raise NotAllowed()

    def rule_lives_quebec(self):
        if not self.quote.driver.province == 'Québec':
            logging.debug("Not allowed, driver not from Quebce")
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
        logging.debug("Not allowed, older than 21")
        raise NotAllowed()
