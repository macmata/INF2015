from builder.rules import Rule


class CreateQuote(Rule):
    PRIORITY = 1

    def rule_build_initial_quote(self):
        print("execution regle 1")
        self.quote.montant = 100

    def rule_deuxieme(self):
        print("execution regle 2")
        self.quote.montant = 200
