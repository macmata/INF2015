import logging

from builder.rules import Rule
from builder.rules import decorators


class ContractRule(Rule):
    PRIORITY = 2

    def rule_contract_more_than_3_years(self):
        if self.quote.contrat.duree == 3:
            logging.debug("Contrat 3 ans, %.2f$ - 15%% = %.2f$" % (
                self.quote.montant/100,
                int(self.quote.montant*0.85)/100
            ))
            self.quote.montant = int(self.quote.montant * 0.85)
