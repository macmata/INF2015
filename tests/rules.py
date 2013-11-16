# -*- coding: utf-8 -*-
import unittest
import os
from datetime import datetime, date, timedelta

from builder.quote import Quotes
from builder.exceptions import NotAllowed

from tests.mock import mock_car, mock_moto, mock_contract, mock_driver

from builder.rules import allowed

class SuccessException(Exception):
    pass


class Allowed(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        self.driver = mock_driver(
            datetime(
                self.today.year - 51,
                self.today.month,
                self.today.day
            ),
            u"Montréal",
            u"Québec",
            "M",
            date(2006, 1, 1),
            True,
            True,
            True,
        )
        self.vehicules = (
            mock_car(
                2014,
                "Porsche",
                "Panamera",
                8000,
                "Sherlock",
                True,
                True
            ),
            mock_moto(
                2013,
                "Ducati",
                "Diavel Dark",
                1500,
                "Sherlock",
                True,
                True
            )
        )

        self.contract = mock_contract(
            3,
            datetime(2013, 11, 16)
        )


        self.quotes = Quotes(self.vehicules, self.driver, self.contract)

        self.rule_car = allowed.Allowed(self.quotes.quotes[0])
        self.rule_moto = allowed.Allowed(self.quotes.quotes[1])

    def test_create_vehicule(self):
        vehicule = self.rule_car.create_vehicule()
        assert vehicule[0] == 2014
        assert vehicule[1] == "Porsche"
        assert vehicule[2] == "Panamera"

    def test_rule_vehicule_exists_moto(self):
        with self.assertRaises(NotAllowed):
            self.rule_moto.quote.vehicule.year = 2014
            self.rule_moto.rule_vehicule_exists_moto()
        self.rule_moto.quote.vehicule.year = 2013

        with self.assertRaises(NotAllowed):
            self.rule_moto.quote.vehicule.model = "Diavel Dark foobar"
            self.rule_moto.rule_vehicule_exists_moto()
        self.rule_moto.quote.vehicule.model = "Diavel Dark"

        with self.assertRaises(NotAllowed):
            self.rule_moto.quote.vehicule.make = "Ducati foobar"
            self.rule_moto.rule_vehicule_exists_moto()
        self.rule_moto.quote.vehicule.make = "Ducati"

        self.rule_moto.rule_vehicule_exists_moto()


    def test_rule_vehicule_exists_car(self):
        with self.assertRaises(NotAllowed):
            self.rule_car.quote.vehicule.year = 2013
            self.rule_car.rule_vehicule_exists_car()
        self.rule_car.quote.vehicule.year = 2014

        with self.assertRaises(NotAllowed):
            self.rule_car.quote.vehicule.model = "Panamera foobar"
            self.rule_car.rule_vehicule_exists_car()
        self.rule_car.quote.vehicule.model = "Panamera"

        with self.assertRaises(NotAllowed):
            self.rule_car.quote.vehicule.make = "Porsche foobar"
            self.rule_car.rule_vehicule_exists_car()
        self.rule_car.quote.vehicule.make = "Porsche"

        self.rule_car.rule_vehicule_exists_car()

    def test_lives_quebec(self):
        self.rule_car.rule_lives_quebec()

        with self.assertRaises(NotAllowed):
            self.rule_car.quote.driver.province = "Alberta"
            self.rule_car.rule_lives_quebec()

    def test_vehicule_more_than_million(self):
        self.rule_car.rule_vehicule_more_than_million()

        self.rule_car.quote.vehicule.value = 1000000
        self.rule_car.quote.vehicule.interior_garage = False
        self.rule_car.quote.vehicule.alarm = False
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_vehicule_more_than_million()

        self.rule_car.quote.vehicule.interior_garage = True
        self.rule_car.quote.vehicule.alarm = False
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_vehicule_more_than_million()

        self.rule_car.quote.vehicule.alarm = True
        self.rule_car.quote.vehicule.interior_garage = False
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_vehicule_more_than_million()

        self.rule_car.quote.vehicule.alarm = True
        self.rule_car.quote.vehicule.interior_garage = True
        self.rule_car.rule_vehicule_more_than_million()

    def test_25_man(self):
        self.rule_car.rule_25_man()

        self.rule_car.quote.driver.birthday = datetime(
            self.today.year - 25,
            self.today.month,
            self.today.day
        )
        self.rule_car.rule_25_man()

        self.rule_car.quote.driver.birthday += timedelta(days=1)
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_25_man()

        self.rule_car.quote.driver.birthday -= timedelta(days=2)
        self.rule_car.rule_25_man()

    def test_21_woman(self):
        self.rule_car.quote.driver.gender = 'F'
        self.rule_car.rule_21_woman()

        self.rule_car.quote.driver.birthday = datetime(
            self.today.year - 21,
            self.today.month,
            self.today.day
        )
        self.rule_car.rule_21_woman()

        self.rule_car.quote.driver.birthday += timedelta(days=1)
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_21_woman()

        self.rule_car.quote.driver.birthday -= timedelta(days=2)
        self.rule_car.rule_21_woman()

    def test_older_75(self):
        self.rule_car.rule_older_75()
        self.rule_car.quote.driver.birthday = datetime(
            self.today.year - 75,
            self.today.month,
            self.today.day
        )
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_older_75()

        self.rule_car.quote.driver.birthday += timedelta(days=1)
        self.rule_car.rule_older_75()

        self.rule_car.quote.driver.birthday -= timedelta(days=2)
        with self.assertRaises(NotAllowed):
            self.rule_car.rule_older_75()


