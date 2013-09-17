
import json,sys

class Conducteur(object):
    def __init__(self):
        self.date_de_naissance = ""
        self.province = ""
        self.ville = ""
        self.sexe = ""
        self.date_fin_cours_de_conduite = ""
        self.cours_de_conduite_reconnus_par_CAA = ""
        self.premier_contrat = ""

    def load_file(self):
        json_data = open(sys.argv[1])
        data = json.load(json_data)
        json_data.close()
        
        return data

    def extract_data_driver(self):
        data = self.load_file()
        self.date_de_naissance  = data["conducteur"]["date_de_naissance"]
        self.province = data["conducteur"]["province"]
        self.ville = data["conducteur"]["ville"]
        self.sexe = data["conducteur"]["sexe"]
        self.date_fin_cours_de_conduite = data["conducteur"]["date_fin_cours_de_conduite"]
        self.cours_de_conduite_reconnus_par_CAA = data["conducteur"]["cours_de_conduite_reconnus_par_CAA"]
        self.premier_contrat = data["conducteur"]["premier_contrat"]
       


#test

driver = Conducteur()
driver.extract_data_driver()

print (driver.date_de_naissance)
print (driver.province)
print (driver.ville)
print (driver.sexe)
print (driver.date_fin_cours_de_conduite)
print (driver.cours_de_conduite_reconnus_par_CAA)
print (driver.premier_contrat)
