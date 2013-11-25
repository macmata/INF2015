# -*- coding: utf-8 -*-
import unittest
import os
from datetime import datetime, date

from tests.mock import mock_driver

class SuccessException(Exception):
    pass

class Driver(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        self.driver = mock_driver(
            datetime(
                self.today.year - 51,
                self.today.month,
                self.today.day
            ),
            "Montréal",
            "Québec",
            "M",
            date(self.today.year - 5, 1, 1),
            True,
            True,
            True,
        )

    def test_age(self):
        self.driver.birthday = datetime(
                self.today.year - 51,
                self.today.month,
                self.today.day
        )
        assert self.driver.age() == 51
        self.driver.birthday += timedelta(days=1)
        assert self.driver.age() == 51
        self.driver.birthday -= timedelta(days=2)
        assert self.driver.age == 50

    def test_years_experience(self):
        self.driver.date_lessons = datetime(
                self.today.year - 15,
                self.today.month,
                self.today.day
        )
        assert self.driver.years_experience() == 15
        self.driver.date_lessons += timedelta(days=1)   
        assert self.driver.years_experience() == 15
        self.driver.date_lessons -= timedelta(days=2)
        assert self.driver.years_experience() == 14
