
import json
from builder import voiture,conducteur

def load_file(input_file):
    json_data = open(input_file)
    data = json.load(json_data)
    json_data.close()
    return data

def extract_data_car(input_file):
    car = voiture.Voiture()
    data = load_file(input_file)
    car.annee  = data["voiture"]["annee"]
    car.marque = data["voiture"]["marque"]
    car.modele = data["voiture"]["modele"]
    car.valeur_des_options = data["voiture"]["valeur_des_options"]
    car.burinage = data["voiture"]["burinage"]
    car.garage_interieur = data["voiture"]["garage_interieur"]
    car.systeme_alarme = data["voiture"]["systeme_alarme"]
    return car    

def extract_data_driver(input_file):
    driver = conducteur.Conducteur()
    data = load_file(input_file)
    driver.date_de_naissance = data["conducteur"]["date_de_naissance"]
    driver.province = data["conducteur"]["province"]
    driver.ville = data["conducteur"]["ville"]
    driver.sexe = data["conducteur"]["sexe"]
    driver.date_fin_cours_de_conduite = data["conducteur"]["date_fin_cours_de_conduite"]
    driver.cours_de_conduite_reconnus_par_CAA = data["conducteur"]["cours_de_conduite_reconnus_par_CAA"]
    driver.premier_contrat = data["conducteur"]["premier_contrat"]
    return driver

def extract_data_all(input_file):
    driver = extract_data_driver(input_file)
    car = extract_data_car(input_file)
    return car,driver

