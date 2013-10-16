import json
from datetime import datetime

from builder.quote import Car, Driver, Contrat

class JsonReader(object):
    def __init__(self, input_file):
        with open(input_file) as file:
            self.data = json.load(file)

    def build_car(self):
        car = Car()
        car.annee  = self.data["voitures"]["annee"]
        car.marque = self.data["voitures"]["marque"]
        car.modele = self.data["voitures"]["modele"]
        car.valeur_des_options = self.data["voitures"]["valeur_des_options"]
        car.burinage = self.data["voitures"]["burinage"]
        car.garage_interieur = self.data["voitures"]["garage_interieur"]
        car.systeme_alarme = self.data["voitures"]["systeme_alarme"]
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

    def build_moto(self):
        moto = Moto()
        moto.annee = ["motos"]["annee"]
        moto.marque = ["motos"]["marque"]
        moto.modele = ["motos"]["modele"]
        moto.valeur_des_options = ["motos"]["valeur_des_options"]
        moto.burinage = ["motos"]["burinage"]
        moto.garage_interieur = ["motos"]["garage_interieur"]
        moto.systeme_alarme = ["motos"]["systeme_alarme"]
        return moto

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

