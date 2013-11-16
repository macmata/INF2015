#from quote import Quote

from builder.rules.vehicules import Cars, Motos

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





    def get_total_quotes(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM soumission"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_not_insured(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM soumission WHERE assurable = 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_insured(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM soumission WHERE assurable != 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_man(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM soumission WHERE gender = 'M'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_woman(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM soumission WHERE gender = 'F'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules(self):
        cursor = self.conn.cursor()
        query = "SELECT count(*) FROM vehicule"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_car_insured(self):
        cursor = self.conn.cursor()
        query = """
            SELECT count(*) FROM vehicule
            INNER JOIN soumission ON soumission.id = vehicul.soumission

            WHERE soumission.assurable = 0 and type = 'car'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_moto_insured(self):
        cursor = self.conn.cursor()
        query = """
            SELECT count(*) FROM vehicule
            INNER JOIN soumission ON soumission.id = vehicule.soumission

            WHERE soumission.assurable = 0 and type = 'moto'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules_by_make(self):
        cursor = self.conn.cursor()

        stats = []
        makes = set()
        for _, make, _ in (Cars + Motos).keys():
            makes.add(make)
        for make in makes:

            query = """
                SELECT count(*) FROM vehicule
                INNER JOIN soumission ON soumission.id = vehicul.soumission

                WHERE soumission.marque = ?
            """
            cursor.execute(query, make)
            stats.append(make, cursor.fetchone())

        return stats
