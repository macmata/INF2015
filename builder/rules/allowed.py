from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder import liste

class Allowed(Rule):
    PRIORITY = 0

    def rule_1(self):
        price = liste.find_car(self.quote.voiture)
        if price == None:
            raise NotAllowed()
        else:
            self.quote.montant = price
            print (price)

    def rule_2(self):
        is_living_here = liste.live_in_quebec(self.quote.conducteur)
              

    def age_ok(self):
        if self.quote.conducteur.sexe == 'M':
            if liste.older_then_x(conducteur,25) == False:
                raise NotAllowed()
        else:
            if liste.older_then_x(conducteur,21) == False:
                raise NotAllowed()
        if liste.too_old(conducteur,75) == True:
                raise NotAllowed()
    
    def rule_4(self):    
        pass
