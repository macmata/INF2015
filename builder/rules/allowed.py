from builder.rules import Rule
from builder.exceptions import NotAllowed


class Allowed(Rule):
    PRIORITY = 0

    def rule_deuxieme(self):
        raise NotAllowed()
