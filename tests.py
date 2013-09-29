import unittest
import os
import datetime

from builder.reader import json
from builder.quote import Driver, Car, Contrat


class JsonReader(unittest.TestCase):

    def setUp(self):
        content = """
        {
            "voiture": {
                "annee": 2014,
                "marque": "Porsche",
                "modele": "911 Carrera",
                "valeur_des_options": 5000.00,
                "burinage": "Patate Frite",
                "garage_interieur": true,
                "systeme_alarme": false
            },
            "conducteur": {
                "date_de_naissance": "1980-01-01",
                "province": "Québec",
                "ville": "Montréal",
                "sexe": "F",
                "date_fin_cours_de_conduite": "2000-12-01",
                "cours_de_conduite_reconnus_par_CAA": true,
                "premier_contrat": false
            },
            "duree_contrat": 3
        }
        """
        self.filename = 'unittest_json'
        with open(self.filename, 'w') as f:
            f.write(content)

    def test_car(self):
        reader = json.JsonReader(self.filename)
        car = reader.build_car()

        assert car.annee == 2014
        assert car.modele == '911 Carrera'
        assert car.marque == 'Porsche'
        assert car.valeur_des_options == 5000
        assert car.burinage == "Patate Frite"
        assert car.garage_interieur
        assert not car.systeme_alarme

    def test_contrat(self):
        reader = json.JsonReader(self.filename)
        contrat = reader.build_contrat()
        assert contrat.duree == 3


    def test_car(self):
        reader = json.JsonReader(self.filename)
        driver = reader.build_driver()

        assert driver.date_de_naissance == datetime.datetime(1980, 1, 1)
        assert driver.date_fin_cours_de_conduite == datetime.datetime(2000, 12, 1)
        assert driver.ville == 'Montréal'
        assert driver.province == 'Québec'
        assert driver.sexe == 'F'
        assert driver.cours_de_conduite_reconnus_par_CAA
        assert not driver.premier_contrat

    def test_get_data(self):
        reader = json.JsonReader(self.filename)
        (driver, car, contrat) = reader.get_data()
        assert isinstance(driver, Driver)
        assert isinstance(car, Car)
        assert isinstance(contrat, Contrat)

    def setDown(self):
        os.unlink(self.filename)


if __name__ == '__main__':
    unittest.main()
