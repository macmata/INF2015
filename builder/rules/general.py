# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators


class GeneralRules(Rule):
    PRIORITY = 2

    def rule_options(self):
        self.quote.montant += int((self.quote.car.valeur_des_options * 100) * 0.10)

    def rule_lives_in(self):
        if self.quote.driver.ville in ('Longueuil', 'Montréal'):
            self.quote.montant += 20000

    def rule_sherlock(self):
        if self.quote.car.burinage == 'Sherlock':
            self.quote.montant -= 25000

    @decorators.woman
    @decorators.braket_age_femme(21,50)
    def rule_woman(self):
        self.quote.montant *= 0.11

    @decorators.woman
    @decorators.braket_age_femme(41,65)
    def rule_woman(self):
        self.quote.montant *= 0.09

    @decorators.woman
    @decorators.braket_age_femme(66,75)
    def rule_woman(self):
        self.quote.montant *= 0.15

    def rule_interior_garage(self):
        if self.quote.car.garage_interieur:
            self.quote.montant -= 50000

    def rule_alarm_system(self):
        if self.quote.car.systeme_alarme:
            self.quote.montant -= 50000

    def rule_cours_conduite_caa(self):
        if self.quote.driver.cours_de_conduite_reconnus_par_CAA:
            self.quote.montant -= 10000

    @decorators.man
    @decorators.younger_than(35)
    def rule_man_less_than_35(self):
        self.quote.montant += 100000

    def rule_premier_contrat(self):
        if self.quote.driver.premier_contrat:
            self.quote.montant += 200000

    def rule_annee_experience(self):
        if self.quote.driver.years_experience > 15:
            self.quote.montant -= 40000
