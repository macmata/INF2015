from builder.rules import Rule
from builder    import liste

class CreateQuote(Rule):
    PRIORITY = 1
    def rule_00(self):
        print("execution regle 1")
        if self.quote.contrat.duree == 3:
            self.quote.montant -= self.quote.montant * 0.15
        self.quote.montant = self.quote.montant * 0.09
    
    def rule_01(self):
        print("execution regle 2")
        self.quote.montant += self.quote.voiture.valeur_des_options * 0.10

    def rule_02(self):
        print("execution regle 3")
        if self.quote.conducteur.ville == "Montréal" or self.quote.conducteur.ville == "Longueuil":
            self.quote.montant += 200

    def rule_03(self):
        print("execution regle 4")
        if self.quote.voiture.burinage == "Sherlock": 
            self.quote.montant -= 250

    def rule_04(self):
        print("execution regle 5")
        if self.quote.conducteur == 'F':
            self.quote.montant -= 1000

    def rule_05(self):
        print("execution regle 6")
        if self.quote.voiture.garage_interieur == True:
            self.quote.montant -= 500

    def rule_06(self):
        print("execution regle 7")
        if self.quote.voiture.systeme_alarme == True:
            self.quote.montant -= 500

    def rule_07(self):
        print("execution regle 8")
        if self.quote.conducteur.cours_de_conduite_reconnus_par_CAA == True:
            self.quote.montant -= 100

    def rule_08(self):
        print("execution regle 9")
        if self.quote.conducteur.sexe == "M":
            if liste.older_then_x(self.quote.conducteur, 35) == False:
                self.quote.montant += 1000

    def rule_09(self):
        if self.quote.conducteur.premier_contrat == "True":
            self.quote.montant += 2000

    def rule_10(self):
        pass
