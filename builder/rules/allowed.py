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
              

    def rule_3(self):
        is_older_than_x = liste.man_older_then_x(self.quote.conducteur,25)
        if is_older_than_x == False:
            raise NotAllowed()
    
    def rule_4(self):    
        pass
