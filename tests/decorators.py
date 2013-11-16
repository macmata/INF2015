# -*- coding: utf-8 -*-
import unittest
import os
import datetime

from builder.quote import Quotes
from tests.mock import mock_car, mock_moto, mock_contract, mock_driver

from builder.rules.decorators import *

class SuccessException(Exception):
    pass


class Decorators(unittest.TestCase):

    def setUp(self):
        self.today = datetime.date.today()
        self.driver = mock_driver(
            datetime.datetime(
                self.today.year - 51,
                self.today.month,
                self.today.day
            ),
            "Montréal",
            "Québec",
            "M",
            datetime.date(2006, 1, 1),
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
            datetime.date(2013, 11, 16)
        )


        self.quotes = Quotes(self.vehicules, self.driver, self.contract)

        class MockObj:
            pass
        self.mock_obj = MockObj
        self.mock_obj.quote = self.quotes.quotes[0]

    def test_man(self):
        @man
        def testing_man(obj):
            raise SuccessException

        with self.assertRaises(SuccessException):
            testing_man(self.mock_obj)

        self.mock_obj.quote.driver.gender = "F"
        testing_man(self.mock_obj)

    def test_woman(self):
        @woman
        def testing_woman(obj):
            raise SuccessException

        with self.assertRaises(SuccessException):
            self.mock_obj.quote.driver.gender = "F"
            testing_woman(self.mock_obj)

        self.mock_obj.quote.driver.gender = "M"
        testing_woman(self.mock_obj)

    def test_moto(self):
        @moto
        def testing_moto(obj):
            raise SuccessException

        self.mock_obj.quote.vehicule = self.vehicules[1]
        with self.assertRaises(SuccessException):
            testing_moto(self.mock_obj)

        self.mock_obj.quote.vehicule = self.vehicules[0]
        testing_moto(self.mock_obj)

    def test_car(self):
        @car
        def testing_car(obj):
            raise SuccessException

        self.mock_obj.quote.vehicule = self.vehicules[0]
        with self.assertRaises(SuccessException):
            testing_car(self.mock_obj)

        self.mock_obj.quote.vehicule = self.vehicules[1]
        testing_car(self.mock_obj)

    def test_older_than(self):
        @older_than(50)
        def testing_older_than(obj):
            raise SuccessException

        with self.assertRaises(SuccessException):
            testing_older_than(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 49,
            self.today.month,
            self.today.day
        )
        testing_older_than(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 51,
            self.today.month,
            self.today.day
        )
        with self.assertRaises(SuccessException):
            testing_older_than(self.mock_obj)

    def test_bracket_age(self):
        @bracket_age(45, 55)
        def testing_bracket_age(obj):
            raise SuccessException

        with self.assertRaises(SuccessException):
            testing_bracket_age(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 45,
            self.today.month,
            self.today.day
        )
        with self.assertRaises(SuccessException):
            testing_bracket_age(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 55,
            self.today.month,
            self.today.day
        )
        with self.assertRaises(SuccessException):
            testing_bracket_age(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 56,
            self.today.month,
            self.today.day
        )
        testing_bracket_age(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 44,
            self.today.month,
            self.today.day
        )
        testing_bracket_age(self.mock_obj)

    def test_younger_than(self):
        @younger_than(51)
        def testing_younger_than(obj):
            raise SuccessException

        testing_younger_than(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 50,
            self.today.month,
            self.today.day
        )
        with self.assertRaises(SuccessException):
            testing_younger_than(self.mock_obj)

        self.mock_obj.quote.driver.birthday = datetime.datetime(
            self.today.year - 52,
            self.today.month,
            self.today.day
        )
        testing_younger_than(self.mock_obj)

    def test_bracket_date(self):
        @braket_date(1, 1, 6, 1)
        def testing_bracket_date(obj):
            raise SuccessException

        testing_bracket_date(self.mock_obj)

        self.mock_obj.quote.contract.starting_date = datetime.date(2013, 1, 1)
        with self.assertRaises(SuccessException):
            testing_bracket_date(self.mock_obj)
        self.mock_obj.quote.contract.starting_date = datetime.date(2013, 6, 1)
        with self.assertRaises(SuccessException):
            testing_bracket_date(self.mock_obj)

        self.mock_obj.quote.contract.starting_date = datetime.date(2013, 2, 15)
        with self.assertRaises(SuccessException):
            testing_bracket_date(self.mock_obj)


        self.mock_obj.quote.contract.starting_date = datetime.date(2013, 6, 2)
        testing_bracket_date(self.mock_obj)
