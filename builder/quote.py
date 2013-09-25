import inspect
from heapq import heappush

from builder import rules
from builder.rules.rule import Rule
from builder.exceptions import NotAllowed


class Quote(object):
    def __init__(self, car, driver, contrat):
        self.car = car
        self.driver = driver
        self.contrat = contrat
        self.montant = 0

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
        try:
            for _, rule in self.rules:
                rule.apply_rules()
        except NotAllowed:
            self.montant = None


class Contrat(object):
    pass


class Driver(object):
    pass


class Car(object):
    pass
