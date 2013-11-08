# -*- coding: utf-8 -*-
import json

Cars = {}
Cars[(2014, u"Porsche", u"Boxter")] = 60000
Cars[(2014, u"Porsche", u"Boxter S")] = 72000
Cars[(2014, u"Porsche", u"Cayman")] = 62000
Cars[(2014, u"Porsche", u"Cayman S")] = 75000
Cars[(2014, u"Porsche", u"911 Carrera")] = 100000
Cars[(2014, u"Porsche", u"911 Carrera S")] = 115000
Cars[(2014, u"Porsche", u"911 Carrera Cabriolet")] = 112000
Cars[(2014, u"Porsche", u"911 Carrera S Cabriolet")] = 129000
Cars[(2014, u"Porsche", u"911 Carrera 4")] = 106000
Cars[(2014, u"Porsche", u"911 Carrera 4S")] = 123000
Cars[(2014, u"Porsche", u"911 Carrera 4 Cabriolet")] = 120000
Cars[(2014, u"Porsche", u"911 Carrera 4S Cabriolet")] = 137000
Cars[(2014, u"Porsche", u"911 50 ans")] = 142000
Cars[(2014, u"Porsche", u"911 Turbo")] = 170000
Cars[(2014, u"Porsche", u"911 Turbo S")] = 207000
Cars[(2014, u"Porsche", u"911 GT3")] = 149000
Cars[(2014, u"Porsche", u"Panamera")] = 90000
Cars[(2014, u"Porsche", u"Panamera 4")] = 95000
Cars[(2014, u"Porsche", u"Panamera S")] = 107000
Cars[(2014, u"Porsche", u"Panamera S E-Hybride")] = 114000
Cars[(2014, u"Porsche", u"Panamera 4S")] = 113000
Cars[(2014, u"Porsche", u"Panamera 4S Executive")] = 144000
Cars[(2014, u"Porsche", u"Paramera GTS")] = 130000
Cars[(2014, u"Porsche", u"Paramera Turbo")] = 162000
Cars[(2014, u"Porsche", u"Paramera Turbo Executive")] = 185000
Cars[(2014, u"Porsche", u"Cayenne")] = 59000
Cars[(2014, u"Porsche", u"Cayenne Diesel")] = 67000
Cars[(2014, u"Porsche", u"Cayenne S")] = 77000
Cars[(2014, u"Porsche", u"Cayenne S Hybride")] = 82000
Cars[(2014, u"Porsche", u"Cayenne GTS")] = 96000
Cars[(2014, u"Porsche", u"Cayenne Turbo")] = 125000
Cars[(2014, u"Porsche", u"Cayenne Turbo S")] = 169000
Cars[(2014, u"Maserati", u"Quattroporte Q4 AWD")] = 119000
Cars[(2014, u"Maserati", u"Quattroporte GTS")] = 148000
Cars[(2013, u"Maserati", u"GranTurismo Sport")] = 140000
Cars[(2012, u"Maserati", u"GranTurismo S - MC SportLine")] = 130000
Cars[(2012, u"Maserati", u"GranTurismo MC Stradale")] = 145000
Cars[(2011, u"Maserati", u"GranTurismo S Convertible")] = 127000
Cars[(2013, u"Ferrari", u"FF")] = 340000
Cars[(2013, u"Ferrari", u"California F1")] = 246000
Cars[(2012, u"Ferrari", u"458 Spyder F1")] = 343000
Cars[(2012, u"Ferrari", u"458 Italia F1")] = 300000
Cars[(2012, u"Ferrari", u"California F1")] = 223000
Cars[(2010, u"Ferrari", u"599GTB Fiorano F1")] = 250000
Cars[(2010, u"Ferrari", u"California F1")] = 189000
Cars[(2009, u"Ferrari", u"Scuderia 16M Spider F1")] = 280000
Cars[(2009, u"Ferrari", u"F4300 Spider F1")] = 180000
Cars[(2006, u"Ferrari", u"F430 Challenge F1")] = 150000
Cars[(2003, u"Ferrari", u"575M Maranello F1")] = 93000
Cars[(1993, u"Ferrari", u"348TS Special - Limited Edition")] = 80000
Cars[(1970, u"Ferrari", u"365 DT 2+2")] = 170000
Cars[(2013, u"Porsche", u"918 Spyder")] = 845000
Cars[(2014, u"Ferrari", u"LaFerrari")] = 1300000
Cars[(2014, u"Lamborghini", u"Reventon")] = 1600000
Cars[(2014, u"Lamborghini", u"Veneno")] = 3900000
Cars[(2014, u"Koenigsegg", u"Agera R")] = 1600000
Cars[(2014, u"Aston Martin", u"One-77")] = 1850000
Cars[(2014, u"Pagini", u"Zonda Cinque Roadster")] = 1800000
Cars[(2014, u"Pagini", u"Huayra")] = 1300000
Cars[(2014, u"Bugatti", u"Veyron Super Sport")] = 2400000
Cars[(2014, u"Bugatti", u"Veyron Grand Sport Vitesse World Record Edition")
        ] = 2600000
Cars[(2014, u"W Motors", u"Lykan HyperSport")] = 3400000

Motos = {}
Motos[(2013, u"Ducati", u"Diavel Dark")] = (1198.4, 19000)
Motos[(2013, u"Ducati", u"Hypermotard SP")] = (821.1, 16000)
Motos[(2013, u"Ducati", u"Monster 1100 Evo")] = (1078, 13500)
Motos[(2013, u"Ducati", u"Streetfighter 848")] = (849, 14300)
Motos[(2013, u"Ducati", u"Superbike 1199 Panigale R")] = (1198, 32000)


class Vehicule(object):
    def show_list(self):
        vehicule_data = [] 
        for car in Cars:
            vehicule_data.append({u"marque": car[1], u"modele":car[2], u"annee": car[0], u"type": u"voiture"})
        for moto in Motos:
            vehicule_data.append({u"marque": moto[1], u"modele": moto[2], u"annee": moto[0], u"type": u"moto"}) 
        data = {u"assurables": vehicule_data} 
        json_file = json.dumps(data, indent=4)
        print(json_file)


class Car(Vehicule):
    pass


class Moto(Vehicule):
    pass

v = Vehicule()
v.show_list()
