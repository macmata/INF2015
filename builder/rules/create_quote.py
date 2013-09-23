# -*- coding: utf-8 -*-

from builder.rules import Rule
from builder import liste

class CreateQuote(Rule):
    PRIORITY = 1
    def rule_00(self):
        print("execution regle 001")
        if self.quote.contrat.duree == 3:
            self.quote.montant -= self.quote.montant * 0.15
        self.quote.montant = self.quote.montant * 0.09

    def rule_001(self):
        print("execution regle 002")
        self.quote.montant += self.quote.voiture.valeur_des_options * 0.10

    def rule_002(self):
        print("execution regle 003")
        if self.quote.conducteur.ville == "Montréal" or self.quote.conducteur.ville == "Longueuil":
            self.quote.montant += 200

    def rule_003(self):
        print("execution regle 004")
        if self.quote.voiture.burinage == "Sherlock":
            self.quote.montant -= 250

    def rule_004(self):
        print("execution regle 005")
        if self.quote.conducteur == 'F':
            self.quote.montant -= 1000

    def rule_005(self):
        print("execution regle 006")
        if self.quote.voiture.garage_interieur == True:
            self.quote.montant -= 500

    def rule_006(self):
        print("execution regle 007")
        if self.quote.voiture.systeme_alarme == True:
            self.quote.montant -= 500

    def rule_007(self):
        print("execution regle 008")
        if self.quote.conducteur.cours_de_conduite_reconnus_par_CAA == True:
            self.quote.montant -= 100

    def rule_008(self):
        print("execution regle 009")
        if self.quote.conducteur.sexe == "M":
            if liste.older_then_x(self.quote.conducteur, 35) == False:
                self.quote.montant += 1000

    def rule_009(self):
        print("execution regle 010")
        if self.quote.conducteur.premier_contrat == True:
            self.quote.montant += 2000

    def rule_010(self):
        print("execution regle 011")
        if liste.more_then_x_experience(self.quote.conducteur,15) == True:
            self.quote.montant -= 400
