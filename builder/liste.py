from builder import load 

def get_list_price():
    list_price = [] 
    list_price.append([2014,"Porsche","Boxter",60000])
    list_price.append([2014,"Porsche","Boxter S",72000])
    list_price.append([2014,"Porsche","Cayman",62000])
    list_price.append([2014,"Porsche","Cayman S",75000])
    list_price.append([2014,"Porsche","911 Carrera",100000])
    list_price.append([2014,"Porsche","911 Carrera S",115000])
    list_price.append([2014,"Porsche","911 Carrera Cabriolet",112000])
    list_price.append([2014,"Porsche","911 Carrera S Cabriolet",129000])
    list_price.append([2014,"Porsche","911 Carrera 4",106000])
    list_price.append([2014,"Porsche","911 Carrera 4S",123000])
    list_price.append([2014,"Porsche","911 Carrera 4 Cabriolet",120000])
    list_price.append([2014,"Porsche","911 Carrera 4S Cabriolet",137000])
    list_price.append([2014,"Porsche","911 50 ans",142000])
    list_price.append([2014,"Porsche","911 Turbo",170000])
    list_price.append([2014,"Porsche","911 Turbo S",207000])
    list_price.append([2014,"Porsche","911 GT3",149000])
    list_price.append([2014,"Porsche","Panamera",90000])
    list_price.append([2014,"Porsche","Panamera 4",95000])
    list_price.append([2014,"Porsche","Panamera S",107000])
    list_price.append([2014,"Porsche","Panamera S E-Hybride",114000])
    list_price.append([2014,"Porsche","Panamera 4S",113000])
    list_price.append([2014,"Porsche","Panamera 4S Executive",144000])
    list_price.append([2014,"Porsche","Paramera GTS",130000])
    list_price.append([2014,"Porsche","Paramera Turbo",162000])
    list_price.append([2014,"Porsche","Paramera Turbo Executive",185000])
    list_price.append([2014,"Porsche","Cayenne",59000])
    list_price.append([2014,"Porsche","Cayenne Diesel",67000])
    list_price.append([2014,"Porsche","Cayenne S",77000])
    list_price.append([2014,"Porsche","Cayenne S Hybride",82000])
    list_price.append([2014,"Porsche","Cayenne GTS",96000])
    list_price.append([2014,"Porsche","Cayenne Turbo",125000])
    list_price.append([2014,"Porsche","Cayenne Turbo S",169000])
    return list_price

def find_car(car):
    data = get_list_price()
    for i in data:
        if i[0] == car.annee:
            if i[1] == car.marque:
                if i[2] == car.modele:
                    price = (i[3])         
        else:
            price = 0            
    return price
