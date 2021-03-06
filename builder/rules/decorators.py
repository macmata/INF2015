from datetime import datetime
from builder.rules.vehicules import Car, Moto


def man(fn):
    def wrapped(obj):
        if obj.quote.driver.gender == 'M':
            return fn(obj)

    return wrapped


def woman(fn):
    def wrapped(obj):
        if obj.quote.driver.gender == 'F':
            return fn(obj)
    return wrapped


def moto(fn):
    def wrapped(obj):
        if isinstance(obj.quote.vehicule, Moto):
            return fn(obj)
    return wrapped


def car(fn):
    def wrapped(obj):
        if isinstance(obj.quote.vehicule, Car):
            return fn(obj)
    return wrapped


class older_than(object):
    def __init__(self, age):
        self.age = age

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.driver.age >= self.age:
                return fn(obj)

        return wrapped


class bracket_age(object):
    def __init__(self, bracket_left, bracket_right):
        self.bracket_left = bracket_left
        self.bracket_right = bracket_right

    def __call__(self, fn):
        def wrapped(obj):
            if self.bracket_left <= obj.quote.driver.age <= self.bracket_right:
                return fn(obj)
        return wrapped


class younger_than(object):
    def __init__(self, age):
        self.age = age

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.driver.age < self.age:
                return fn(obj)

        return wrapped

class braket_date(object):
    def __init__(self, month_l, day_l, month_r, day_r):
        self.month_l = month_l
        self.month_r = month_r
        self.day_l = day_l
        self.day_r = day_r

    def __call__(self, fn):
        def wrapped(obj):
            starting_date = obj.quote.contract.starting_date
            left_date = datetime(starting_date.year, self.month_l, self.day_l)
            right_date = datetime(starting_date.year, self.month_r, self.day_r)
            if left_date <= starting_date <= right_date:
                return fn(obj)
        return wrapped
