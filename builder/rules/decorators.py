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


class older_than(object):
    def __init__(self, age):
        self.age = age

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.driver.age > self.age:
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
