#from quote import Quote
import sqlite3
from array import array




class bdstats(objet):
    def __init__(self,db_file):


    def creat_connection(self,db_file):
        return connection = sqlite3.connect(db_file)

    def create_cursor(self,connection):
        return cursor = connection.cursor()

    def create_table(self,cursor):
        cursor.execute('''CREATE TABLE sousmission
                     (id INTEGER PRIMARY KEY, gender TEXT, assurable int,  )''')
        cursor.execute('''create TABLE vehicules (id INTEGER PRIMARY KEY,marque TEXT, soumission INTEGER REFERENCES SOUMISSION (id), type TEXT)''')

    def insert_toTable(self,cursor,quote):
        cursor.execute("INSERT INTO stocks VALUES ()")

    def extract_qteModel(self,model):
        #curseur.execute('SELECT * FROM Genre WHERE id=?', ids)

    def prep_quote_forTable(self,quote):
        prepQuote = []
        if quote.cars.len < 3;
            for i in quote.cars
                prepQuote[i].append(quote.cars[i])
            for i range(3- quote.cars.len):

                prepQuote.append("null")










    def table_commit(self):
        connection.commit()

    def table_close(self,connection):
        connection.close()






"nb soumision"
"nb soumission non assurable"
"qte homme"
"qte femme"
"nb vehicule"
"nb voiture"
"nb moto"
"vehicule par marque"


