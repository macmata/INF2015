# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class GeneralRules(Rule):
    PRIORITY = 3

    @decorators.moto
    def rule_moto_1000cc(self):
        if self.quote.vehicule.cc > 1000:
            self.quote.montant += 100000

    def rule_vehicule_plus_500000(self):
        if self.quote.vehicule.value > 500000:
            self.quote.montant += 250000

    def rule_options(self):
        self.quote.montant += \
            int((self.quote.vehicule.valeur_des_options * 100) * 0.10)

    def rule_lives_in(self):
        if self.quote.driver.ville in (u'Longueuil', u'Montréal'):
            self.quote.montant += 20000

    def rule_sherlock(self):
        if self.quote.vehicule.burinage == 'Sherlock':
            self.quote.montant -= 25000

    def rule_interior_garage(self):
        if self.quote.vehicule.garage_interieur:
            self.quote.montant -= 50000

    def rule_alarm_system(self):
        if self.quote.vehicule.systeme_alarme:
            self.quote.montant -= 50000

    def rule_cours_conduite_caa(self):
        if self.quote.driver.cours_de_conduite_reconnus_par_CAA:
            self.quote.montant -= 10000

    def rule_premier_contrat(self):
        if self.quote.driver.premier_contrat:
            self.quote.montant += 200000

    def rule_annee_experience(self):
        if self.quote.driver.years_experience > 15:
            self.quote.montant -= 40000

