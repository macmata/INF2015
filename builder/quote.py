import inspect
from datetime import date
from heapq import heappush, heappop
import logging

from builder import rules
from builder.rules.rule import Rule
from builder.exceptions import NotAllowed
from builder.rules.vehicules import Vehicule, Car, Moto


class Quotes(object):
    def __init__(self, vehicules, driver, contract):
        self.quotes = []
        for vehicule in vehicules:
            quote = Quote(vehicule, driver, contract)
            logging.debug("Vehicule %s %s %s" % (
                vehicule.make,
                vehicule.model,
                vehicule.year
            ))
            quote.build_quote()
            self.quotes.append(quote)

    @property
    def monthly_amount(self):
        if self.assurable:
            return round(
                sum([q.monthly_amount for q in self.quotes if q.assurable]),
                2
            )

    @property
    def yearly_amount(self):
        if self.assurable:
            return round(
                sum([q.yearly_amount for q in self.quotes if q.assurable]),
                2
            )

    @property
    def assurable(self):
        return all([q.assurable for q in self.quotes])


class Quote(object):
    def __init__(self, vehicule, driver, contract):
        self.vehicule = vehicule
        self.driver = driver
        self.contract = contract
        self.amount = 0

        self.rules = []
        self.find_rules()

    def find_rules(self):
        for name, module in inspect.getmembers(rules, inspect.ismodule):
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, Rule) and obj != Rule:
                    rule = obj(self)
                    if not hasattr(rule, 'PRIORITY'):
                        priority = 0
                    else:
                        priority = rule.PRIORITY
                    heappush(self.rules, (priority, rule))

    def build_quote(self):
        self.assurable = True
        try:
            while self.rules:
                _, rule = heappop(self.rules)
                rule.apply_rules()
        except NotAllowed:
            self.amount = 0
            self.assurable = False

    @property
    def monthly_amount(self):
        if self.assurable > 0:
            return round(((self.amount * 1.015) / 12) / 100, 2)

    @property
    def yearly_amount(self):
        if self.assurable:
            return round(self.amount / 100, 2)


class Contract(object):
    pass


class Driver(object):
    @property
    def age(self):
        today = date.today()
        birthday = self.birthday

        if today.month < birthday.month or \
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year

    @property
    def years_experience(self):
        today = date.today()
        birthday = self.date_end_of_driving_lessons

        if today.month < birthday.month or \
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year
