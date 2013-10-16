# -*- coding: utf-8 -*-
import pdb
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
CARS[(2014,"Maserati","Quattroporte Q4 AWD")] = 119000
CARS[(2014,"Maserati","Quattroporte GTS")] = 148000
CARS[(2013,"Maserati","GranTurismo Sport")] = 140000
CARS[(2012,"Maserati","GranTurismo S - MC SportLine")] = 130000
CARS[(2012,"Maserati","GranTurismo MC Stradale")] = 145000
CARS[(2011,"Maserati","GranTurismo S Convertible")] = 127000
CARS[(2013,"Ferrari","FF")] = 340000
CARS[(2013,"Ferrari","California F1")] = 246000
CARS[(2012,"Ferrari","458 Spyder F1")] = 343000
CARS[(2012,"Ferrari","458 Italia F1")] = 300000
CARS[(2012,"Ferrari","California F1")] = 223000
CARS[(2010,"Ferrari","599GTB Fiorano F1")] = 250000
CARS[(2010,"Ferrari","California F1")] = 189000
CARS[(2009,"Ferrari","Scuderia 16M Spider F1")] = 280000
CARS[(2009,"Ferrari","F4300 Spider F1")] = 180000
CARS[(2006,"Ferrari","F430 Challenge F1")] = 150000
CARS[(2003,"Ferrari","575M Maranello F1")] = 93000
CARS[(1993,"Ferrari","348TS Special - Limited Edition")] = 80000
CARS[(1970,"Ferrari","365 DT 2+2")] = 170000
CARS[(2013,"Porsche","918 Spyder")] = 845000

MOTOS = {}
MOTOS[(2013,"Ducati","Diavel Dark","1198.4cc")] = 19000
MOTOS[(2013,"Ducati","Hypermotard SP","821.1cc")] = 16000
MOTOS[(2013,"Ducati","Monster 1100 Evo","1078cc")] = 13500
MOTOS[(2013,"Ducati","Streetfighter 848","849cc")] = 14300
MOTOS[(2013,"Ducati","Superbike 1199 Panigale R","1198cc")] = 32000

class Allowed(Rule):
    PRIORITY = 0

    def rule_car_allowed(self):
        car = (
            self.quote.car.annee,
            self.quote.car.marque,
            self.quote.car.modele
        )
        #pdb.set_trace()
        if car in CARS:
            self.quote.car.value = CARS[car]
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
