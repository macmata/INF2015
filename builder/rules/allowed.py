from builder.rules import Rule


class Allowed(Rule):
    PRIORITY = 0

    def rule_deuxieme(self):
        print("execution regle de allowed")
        self.quote.montant = 200
