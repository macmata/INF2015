from builder.rules import Rule


class CreateQuote(Rule):
    PRIORITY = 1

    def rule_build_initial_quote(self):
        self.quote.montant = 100
