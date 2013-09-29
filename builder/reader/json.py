import json
from datetime import datetime

from builder.quote import Car, Driver, Contrat

class JsonReader(object):
    def __init__(self, input_file):
        with open(input_file) as file:
            self.data = json.load(file)

    def build_car(self):
        car = Car()
        car.annee  = self.data["voiture"]["annee"]
        car.marque = self.data["voiture"]["marque"]
        car.modele = self.data["voiture"]["modele"]
        car.valeur_des_options = self.data["voiture"]["valeur_des_options"]
        car.burinage = self.data["voiture"]["burinage"]
        car.garage_interieur = self.data["voiture"]["garage_interieur"]
        car.systeme_alarme = self.data["voiture"]["systeme_alarme"]
        return car

    def build_driver(self):
        driver = Driver()
        driver.date_de_naissance = datetime.strptime(self.data["conducteur"]["date_de_naissance"], "%Y-%m-%d")
        driver.ville = self.data["conducteur"]["ville"]
        driver.province = self.data["conducteur"]["province"]
        driver.sexe = self.data["conducteur"]["sexe"]
        driver.date_fin_cours_de_conduite = datetime.strptime(self.data["conducteur"]["date_fin_cours_de_conduite"], "%Y-%m-%d")
        driver.cours_de_conduite_reconnus_par_CAA = self.data["conducteur"]["cours_de_conduite_reconnus_par_CAA"]
        driver.premier_contrat = self.data["conducteur"]["premier_contrat"]
        return driver

    def build_contrat(self):
        contrat = Contrat()
        contrat.duree = self.data["duree_contrat"]
        return contrat

    def get_data(self):
        return (
                self.build_driver(),
                self.build_car(),
                self.build_contrat()
        )

