# -*- coding: utf-8 -*-
import unittest
import os
import datetime

from builder.reader import json_reader
from builder.quote import Driver, Car, Contract, Moto


class JsonReader(unittest.TestCase):

    def setUp(self):
        content = """
        {
        "voitures": [
        {
        "annee": 2013,
        "marque": "Porsche",
        "modele": "918 Spyder",
        "valeur_des_options": 8000,
        "burinage": "PROACTIF",
        "garage_interieur": true,
        "systeme_alarme": false
    },
    {
        "annee": 2012,
        "marque": "Ferrari",
        "modele": "458 Spyder F1",
        "valeur_des_options": 12000,
        "burinage": "Sherlock",
        "garage_interieur": true,
        "systeme_alarme": true
    }
    ],
        "motos": [
        {
            "annee": 2013,
            "marque": "Ducati",
            "modele": "Hypermotard SP",
            "valeur_des_options": 1000,
            "burinage": "null",
            "garage_interieur": false,
            "systeme_alarme": false
        }
    ],
        "conducteur": {
            "date_de_naissance": "1977-01-15",
            "province": "Quebec",
            "ville": "Montreal",
            "sexe": "M",
            "date_fin_cours_de_conduite": "2000-12-01",
            "cours_de_conduite_reconnus_par_CAA": true,
            "premier_contrat": false,
            "membre_oiq": true
        },
        "duree_contrat": 3
        }
        """
        self.filename = 'unittest_json'
        with open(self.filename, 'w') as f:
            f.write(content)

    def test_car(self):
        reader = json_reader.JsonReader(self.filename)
        car = []
        car = reader.build_car()
        assert car[0].year == 2013
        assert car[0].model == '918 Spyder'
        assert car[0].make == 'Porsche'
        assert car[0].option_value == 8000
        assert car[0].chiseling == 'PROACTIF'
        assert car[0].interior_garage
        assert not car[0].alarm
        assert car[1].year == 2012
        assert car[1].model == '458 Spyder F1'
        assert car[1].make == 'Ferrari'
        assert car[1].option_value == 12000
        assert car[1].chiseling == 'Sherlock'
        assert car[1].interior_garage
        assert car[1].alarm

    def test_motos(self):
        reader = json_reader.JsonReader(self.filename)
        moto = []
        moto = reader.build_moto()
        assert moto[0].year == 2013
        assert moto[0].make == 'Ducati'
        assert moto[0].model == 'Hypermotard SP'
        assert moto[0].option_value == 1000
        assert moto[0].chiseling == 'null'
        assert not moto[0].interior_garage
        assert not moto[0].alarm

    def test_contract(self):
        reader = json_reader.JsonReader(self.filename)
        contract = reader.build_contract()
        assert contract.length == 3


    def test_personne(self):
        reader = json_reader.JsonReader(self.filename)
        driver = reader.build_driver()

        assert driver.birthday == datetime.datetime(1977,1, 15)
        assert driver.date_end_of_driving_lessons == datetime.datetime(2000,12,01)
        assert driver.city == 'Montreal'
        assert driver.province == 'Quebec'
        assert driver.gender == 'M'
        assert driver.driving_lessons_caa
        assert not driver.first_contract
        assert driver.oiq_member

    def test_get_data(self):
        reader = json_reader.JsonReader(self.filename)
        (driver, car, moto, contrat) = reader.get_data()
        assert isinstance(driver, Driver)
        assert isinstance(car[0], Car)
        assert isinstance(car[1], Car)
        assert isinstance(contrat, Contract)
        assert isinstance(moto[0], Moto)

    def setDown(self):
        os.unlink(self.filename)


if __name__ == '__main__':
    unittest.main()
