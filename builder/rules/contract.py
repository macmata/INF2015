import logging

from builder.rules import Rule
from builder.rules import decorators


class ContractRule(Rule):
    PRIORITY = 2

    def rule_contract_more_than_3_years(self):
        if self.quote.contract.length == 3:
            logging.debug("Contrat 3 ans, %.2f$ - 15%% = %.2f$" % (
                self.quote.amount/100,
                self.quote.amount*0.85/100
            ))
            self.quote.amount = self.quote.amount * 0.85
