import json
from datetime import datetime
from builder.quote import Car, Driver, Contrat, Moto

class JsonReader(object):
    def __init__(self, input_file):
        with open(input_file) as file:
            self.data = json.load(file)

    def build_car(self):
        cars = []
        for car_data in self.data["voitures"]:
            car = Car()
            car.annee  = car_data["annee"]
            car.marque = car_data["marque"]
            car.modele = car_data["modele"]
            car.valeur_des_options = car_data["valeur_des_options"]
            car.burinage = car_data["burinage"]
            car.garage_interieur = car_data["garage_interieur"]
            car.systeme_alarme = car_data["systeme_alarme"]
            cars.append(car)
        return cars

    def build_moto(self):
        motos = []
        for moto_data in self.data["motos"]:
            moto = Moto()
            moto.annee = moto_data["annee"]
            moto.marque = moto_data["marque"]
            moto.modele = moto_data["modele"]
            moto.valeur_des_options = moto_data["valeur_des_options"]
            moto.burinage = moto_data["burinage"]
            moto.garage_interieur = moto_data["garage_interieur"]
            moto.systeme_alarme = moto_data["systeme_alarme"]
            motos.append(moto)
        return motos

    def build_driver(self):
        driver = Driver()
        driver.date_de_naissance = datetime.strptime(self.data["conducteur"]["date_de_naissance"], "%Y-%m-%d")
        driver.ville = self.data["conducteur"]["ville"]
        driver.province = self.data["conducteur"]["province"]
        driver.sexe = self.data["conducteur"]["sexe"]
        driver.date_fin_cours_de_conduite = datetime.strptime(self.data["conducteur"]["date_fin_cours_de_conduite"], "%Y-%m-%d")
        driver.cours_de_conduite_reconnus_par_CAA = self.data["conducteur"]["cours_de_conduite_reconnus_par_CAA"]
        driver.premier_contrat = self.data["conducteur"]["premier_contrat"]
        driver.membre_oiq = self.data["conducteur"]["membre_oiq"]
        return driver

    def build_contrat(self):
        contrat = Contrat()
        contrat.duree = self.data["duree_contrat"]
        return contrat

    def get_data(self):
        return (
                self.build_driver(),
                self.build_car(),
                self.build_moto(),
                self.build_contrat()
        )
