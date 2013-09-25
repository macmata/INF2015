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


class burinage(object):
    def __init__(self, company):
        self.company = company

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.car.burinage == self.company:
                return fn(obj)

        return wrapped


def interior_garage(fn):
    def wrapped(obj):
        if obj.quote.car.garage_interieur:
            obj.quote.montant -= 500


class lives_in(object):
    def __init__(self, value):
        if not isinstance(value, tuple):
            self.cities = (value, )
        else:
            self.cities = value

    def __call__(self, fn):
        def wrapped(obj):
            if obj.quote.driver.ville in self.cities:
                return fn(obj)

        return wrapped
