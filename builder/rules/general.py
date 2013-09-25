# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder.rules import decorators
from builder import liste


class GeneralRules(Rule):
    PRIORITY = 2

    def rule_001(self):
        print("execution regle 002")
        self.quote.montant += self.quote.car.valeur_des_options * 0.10

    @decorators.lives_in('Montréal', 'Québec')
    def rule_lives_in(self):
        self.quote.montant += 200

    @decorators.burinage('Sherlock')
    def rule_sherlock(self):
        self.quote.montant -= 250

    @decorators.woman
    def rule_004(self):
        self.quote.montant -= 1000

    @decorators.interior_garage
    def rule_005(self):
        self.quote.montant -= 500

    def rule_006(self):
        print("execution regle 007")
        if self.quote.car.systeme_alarme:
            self.quote.montant -= 500

    def rule_007(self):
        print("execution regle 008")
        if self.quote.driver.cours_de_conduite_reconnus_par_CAA:
            self.quote.montant -= 100

    @decorators.man
    def rule_008(self):
        print("execution regle 009")
        if not liste.older_then_x(self.quote.driver, 35):
            self.quote.montant += 1000

    def rule_009(self):
        print("execution regle 010")
        if self.quote.driver.premier_contrat:
            self.quote.montant += 2000

    def rule_010(self):
        print("execution regle 011")
        if liste.more_then_x_experience(self.quote.driver, 15):
            self.quote.montant -= 400
