from builder.quote import Car, Moto


def man(fn):
    def wrapped(obj):
        if obj.quote.driver.sexe == 'M':
            return fn(obj)

    return wrapped


def woman(fn):
    def wrapped(obj):
        if obj.quote.driver.sexe == 'F':
            return fn(obj)
    return wrapped


def is_moto(fn):
    def wrapped(obj):
        if isinstance(obj, Moto):
            return fn(obj)


def is_car(fn):
    def wrapped(obj):
        if isinstance(obj, Car):
            return fn(obj)


class older_than(object):
    def __init__(self, age):
        self.age = age

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.driver.age > self.age:
                return fn(obj)

        return wrapped


class braket_age(object):
    def __init__(self, braket_left, braket_right):
        self.braket_left = braket_left
        self.braket_right = braket_right

    def __call__(self, fn):
        def wrapped(obj):
            if self.braket_left > obj.quote.driver.age < self.braket_right:
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
