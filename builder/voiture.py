import json,sys

class Voiture(object):
    def __init__(self):
        self.annee  = "" 
        self.marque = ""
        self.modele = ""
        self.valeur_des_options = ""
        self.burinage = ""
        self.garage_interieur = ""
        self.systeme_alarme = ""
                
    def load_file(self):
        json_data = open(sys.argv[1])
        data = json.load(json_data)
        json_data.close()
        
        return data

    def extract_data_car(self):
        data = self.load_file()
        self.annee  = data["voiture"]["annee"]
        self.marque = data["voiture"]["marque"]
        self.modele = data["voiture"]["modele"]
        self.valeur_des_options = data["voiture"]["valeur_des_options"]
        self.burinage = data["voiture"]["burinage"]
        self.garage_interieur = data["voiture"]["garage_interieur"]
        self.systeme_alarme = data["voiture"]["systeme_alarme"]
       


voiture = Voiture()
voiture.extract_data_car()

#test

print (voiture.annee)
print (voiture.marque)
print (voiture.modele)
print (voiture.valeur_des_options)
print (voiture.burinage)
print (voiture.garage_interieur)
print (voiture.systeme_alarme)
