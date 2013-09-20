from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder import liste

class Allowed(Rule):
    PRIORITY = 0

    def rule_1(self):
        price = liste.find_car(self.quote.voiture)
        if price != 0:
            self.quote.mantant = price
        else:
            print("Car not on the list")
            raise NotAllowed()

    def rule_2(self):
        if liste.live_in_quebec(self.quote.conducteur)==False:
            print("Don't live in Quebec")
            raise NotAllowed()

    def rule_3(self):
        if self.quote.conducteur.sexe == 'M':
            if liste.older_then_x(self.quote.conducteur,25) == False:
                print("Men to young")
                raise NotAllowed()
        else:
            if liste.older_then_x(self.quote.conducteur,21) == False:
                print("Girl to young")
                raise NotAllowed()
        if liste.too_old(self.quote.conducteur,75) == True:
                print ("Too old")
                raise NotAllowed()
             
