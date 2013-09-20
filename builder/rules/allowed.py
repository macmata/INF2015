from builder.rules import Rule
from builder.exceptions import NotAllowed
from builder import liste

class Allowed(Rule):
    PRIORITY = 0

    def rule_deuxieme(self):
        price = liste.find_car(self.quote.voiture)
        if price == None:
            raise NotAllowed()
        else:
            self.quote.montant = price
            print (price)

