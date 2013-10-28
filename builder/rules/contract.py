import logging

from builder.rules import Rule
from builder.rules import decorators


class ContractRule(Rule):
    PRIORITY = 1

    def rule_contract_more_than_3_years(self):
        if self.quote.contract.length == 3:
            logging.debug("Contrat 3 ans, %.2f$ - 15%% = %.2f$" % (
                self.quote.vehicule.value/100,
                int(self.quote.vehicule.value*0.85)/100
            ))
            self.quote.vehicule.value = int(self.quote.vehicule.value * 0.85)
