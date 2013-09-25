from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder import liste


class Allowed(Rule):
    PRIORITY = 0

    def rule_car_allowed(self):
        price = liste.find_car(self.quote.car)
        if price != 0:
            self.quote.car.value = price
        else:
            print("Car not on the list")
            raise NotAllowed()

    def rule_lives_quebec(self):
        if not liste.live_in_quebec(self.quote.driver):
            print("Don't live in Quebec")
            raise NotAllowed()

    def rule_gender_age(self):
        if self.quote.driver.sexe == 'M':
            if not liste.older_then_x(self.quote.driver, 25):
                print("Men to young")
                raise NotAllowed()
        else:
            if not liste.older_then_x(self.quote.driver, 21):
                print("Girl to young")
                raise NotAllowed()
        if liste.too_old(self.quote.driver, 75):
                print ("Too old")
                raise NotAllowed()
