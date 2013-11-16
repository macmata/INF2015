# -*- coding: utf-8 -*-
import unittest
import os
from datetime import datetime, date

from mock import mock_driver
from builder    import quote

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
        assert self.driver.age == 51

    def test_years_experience(self):
        assert self.driver.years_experience == 5
