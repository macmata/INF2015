from builder.rules.vehicules import Cars, Motos

import sqlite3
import os

class Stats(objet):
    def __init__(self,db_file):

        if os.path.exists(db_file):
             f = file(db_file)
        else:
            f = file(de_file)
        self.connection = sqlite3.connect(db_file)

    def create_table(self,cursor):
        cursor.execute('''CREATE TABLE sousmission
                     (id INTEGER PRIMARY KEY, gender TEXT, assurable int,  )''')

        cursor.execute('''create TABLE vehicules (id INTEGER PRIMARY KEY,marque TEXT, soumission INTEGER REFERENCES SOUMISSION (id), type TEXT)''')

    def get_total_quotes(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM soumission"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_not_insured(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM soumission WHERE assurable = 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_insured(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM soumission WHERE assurable != 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_man(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM soumission WHERE gender = 'M'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_woman(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM soumission WHERE gender = 'F'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM vehicule"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_car_insured(self):
        cursor = self.connection.cursor()
        query = """
            SELECT count(*) FROM vehicule
            INNER JOIN soumission ON soumission.id = vehicule.soumission

            WHERE soumission.assurable = 0 and type = 'car'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_moto_insured(self):
        cursor = self.connection.cursor()
        query = """
            SELECT count(*) FROM vehicule
            INNER JOIN soumission ON soumission.id = vehicule.soumission

            WHERE soumission.assurable = 0 and type = 'moto'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules_by_make(self):
        cursor = self.connection.cursor()

        stats = []
        makes = set()
        for _, make, _ in (Cars + Motos).keys():
            makes.add(make)
        for make in makes:

            query = """
                SELECT count(*) FROM vehicule
                INNER JOIN soumission ON soumission.id = vehicule.soumission

                WHERE soumission.marque = ?
            """
            cursor.execute(query, (make,))
            stats.append(make, cursor.fetchone())

        return stats

    def insert_quote(self, gender, insured):
        cursor = self.connection.cursor()

        query = "INSERT INTO soumission (gender, assurable) VALUES(?, ?)"
        cursor.execute(query, (gender, insured))
        self.connection.commit()
        return cursor.lastrowid

    def insert_vehicule(self, quote_id, make, vehicule_type):
        cursor = self.connection.cursor()

        query = "INSERT INTO vehicule (marque, soumission, type) VALUES(?, ?, ?)"
        cursor.execute(query, (make, quote_id, vehicule_type))
        self.connection.commit()
        return cursor.lastrowid


