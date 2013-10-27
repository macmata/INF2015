# -*- coding: utf-8 -*-
import unittest
import os
import datetime

from builder.reader import json_reader
from builder.quote import Driver, Car, Contrat, Moto


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
        assert car[0].annee == 2013
        assert car[0].modele == '918 Spyder'
        assert car[0].marque == 'Porsche'
        assert car[0].valeur_des_options == 8000
        assert car[0].burinage == 'PROACTIF'
        assert car[0].garage_interieur
        assert not car[0].systeme_alarme
        assert car[1].annee == 2012
        assert car[1].modele == '458 Spyder F1'
        assert car[1].marque == 'Ferrari'
        assert car[1].valeur_des_options == 12000
        assert car[1].burinage == 'Sherlock'
        assert car[1].garage_interieur
        assert car[1].systeme_alarme

    def test_motos(self):
        reader = json_reader.JsonReader(self.filename)
        moto = []
        moto = reader.build_moto()
        assert moto[0].annee == 2013
        assert moto[0].marque == 'Ducati'
        assert moto[0].modele == 'Hypermotard SP'
        assert moto[0].valeur_des_options == 1000
        assert moto[0].burinage == 'null'
        assert not moto[0].garage_interieur
        assert not moto[0].systeme_alarme

    def test_contrat(self):
        reader = json_reader.JsonReader(self.filename)
        contrat = reader.build_contrat()
        assert contrat.duree == 3


    def test_personne(self):
        reader = json_reader.JsonReader(self.filename)
        driver = reader.build_driver()

        assert driver.date_de_naissance == datetime.datetime(1977,1, 15)
        assert driver.date_fin_cours_de_conduite == datetime.datetime(2000,12,1)
        assert driver.ville == 'Montreal'
        assert driver.province == 'Quebec'
        assert driver.sexe == 'M'
        assert driver.cours_de_conduite_reconnus_par_CAA
        assert not driver.premier_contrat
        assert driver.membre_oiq

    def test_get_data(self):
        reader = json_reader.JsonReader(self.filename)
        (driver, car, moto, contrat) = reader.get_data()
        assert isinstance(driver, Driver)
        assert isinstance(car[0], Car)
        assert isinstance(car[1], Car)
        assert isinstance(contrat, Contrat)
        assert isinstance(moto[0], Moto)

    def setDown(self):
        os.unlink(self.filename)


if __name__ == '__main__':
    unittest.main()
