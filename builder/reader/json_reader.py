from __future__ import unicode_literals

import json
from datetime import datetime
from builder.quote import Car, Driver, Contract, Moto


class JsonReader(object):
    def __init__(self, input_file):
        with open(input_file) as file:
            self.data = json.load(file)

    def build_car(self):
        cars = []
        for car_data in self.data["voitures"]:
            car = Car()
            car.year = car_data["annee"]
            car.make = car_data["marque"]
            car.model = car_data["modele"]
            car.option_value = car_data["valeur_des_options"]
            car.chiseling = car_data["burinage"]
            car.interior_garage = car_data["garage_interieur"]
            car.alarm = car_data["systeme_alarme"]
            cars.append(car)
        return cars

    def build_moto(self):
        motos = []
        for moto_data in self.data["motos"]:
            moto = Moto()
            moto.year = moto_data["annee"]
            moto.make = moto_data["marque"]
            moto.model = moto_data["modele"]
            moto.option_value = moto_data["valeur_des_options"]
            moto.chiseling = moto_data["burinage"]
            moto.interior_garage = moto_data["garage_interieur"]
            moto.alarm = moto_data["systeme_alarme"]
            motos.append(moto)
        return motos

    def build_driver(self):
        driver = Driver()
        driver.birthday = datetime.strptime(
            self.data["conducteur"]["date_de_naissance"], "%Y-%m-%d"
        )
        driver.city = self.data["conducteur"]["ville"]
        driver.province = self.data["conducteur"]["province"]
        driver.gender = self.data["conducteur"]["sexe"]
        driver.date_end_of_driving_lessons = datetime.strptime(
            self.data["conducteur"]["date_fin_cours_de_conduite"], "%Y-%m-%d"
        )
        driver.driving_lessons_caa = \
            self.data["conducteur"]["cours_de_conduite_reconnus_par_CAA"]
        driver.first_contract = self.data["conducteur"]["premier_contrat"]
        driver.oiq_member = self.data["conducteur"]["membre_oiq"]
        return driver

    def build_contract(self):
        contract = Contract()
        contract.length = self.data["duree_contrat"]
        contract.starting_date = datetime.strptime(
                self.data["date_debut"], "%Y-%m-%d")
        return contract

    def get_data(self):
        return (
            self.build_driver(),
            self.build_car(),
            self.build_moto(),
            self.build_contract()
        )
