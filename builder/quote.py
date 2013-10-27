import inspect
from datetime import date
from heapq import heappush, heappop
from builder import rules
from builder.rules.rule import Rule
from builder.exceptions import NotAllowed
from builder.rules.vehicules import Vehicule, Car, Moto


class Quotes(object):
    def __init__(self, vehicules, driver, contrat):
        self.quotes = []
        for vehicule in vehicules:
            quote = Quote(vehicule, driver, contrat)
            quote.build_quote()
            self.quotes.append(quote)

    @property
    def montant_mensuel(self):
        if self.assurable:
            return round(
                sum([q.montant_mensuel for q in self.quotes if q.assurable]),
                2
            )

    @property
    def montant_annuel(self):
        if self.assurable:
            return round(
                sum([q.montant_annuel for q in self.quotes if q.assurable]),
                2
            )

    @property
    def assurable(self):
        return all([q.assurable for q in self.quotes])


class Quote(object):
    def __init__(self, vehicule, driver, contrat):
        self.vehicule = vehicule
        self.driver = driver
        self.contrat = contrat
        self.montant = 0
        self.montantTotal = 0

        self.rules = []
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
            self.montant = 0
            self.assurable = False
            self.montantTotal = 0

    @property
    def montant_mensuel(self):
        if self.assurable > 0:
            return round(((self.montant * 1.015) / 12) / 100, 2)

    @property
    def montant_annuel(self):
        if self.assurable:
            return round(self.montant / 100, 2)


class Contrat(object):
    pass


class Driver(object):
    @property
    def age(self):
        today = date.today()
        birthday = self.date_de_naissance

        if today.month < birthday.month or \
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year

    @property
    def years_experience(self):
        today = date.today()
        birthday = self.date_fin_cours_de_conduite

        if today.month < birthday.month or \
                (today.month == birthday.month and today.day < birthday.day):
            return today.year - birthday.year - 1
        else:
            return today.year - birthday.year
