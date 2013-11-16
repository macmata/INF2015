from builder.rules.vehicules import Cars, Motos, Car, Moto

import sqlite3
import os

class Stats:
    def __init__(self, db_file):
        create_table = False
        if not os.path.exists(db_file):
            open(db_file, 'a').close()
            create_table = True
        f = file(db_file)
        self.connection = sqlite3.connect(db_file)
        if create_table:
            self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE quotes
            (id INTEGER PRIMARY KEY, gender TEXT, insured int);
        ''')
        cursor.execute('''
            CREATE INDEX quotes_gender_index ON quotes (gender);
        ''')
        cursor.execute('''
            CREATE INDEX quotes_insured_index ON quotes (insured);
        ''')

        cursor.execute('''
            CREATE TABLE vehicules
            (
                id INTEGER PRIMARY KEY, make TEXT,
                quote_id INTEGER REFERENCES quotes (id), type TEXT
            )
        ''')
        cursor.execute('''
            CREATE INDEX vehicules_make_index ON vehicules (make);
        ''')
        cursor.execute('''
            CREATE INDEX vehicules_quote_index ON vehicules (quote_id);
        ''')
        cursor.execute('''
            CREATE INDEX vehicules_type_index ON vehicules (type);
        ''')
        self.connection.commit()

    def get_total_quotes(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM quotes"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_not_insured(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM quotes WHERE insured = 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_insured(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM quotes WHERE insured != 0"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_man(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM quotes WHERE gender = 'M'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_quotes_woman(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM quotes WHERE gender = 'F'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules(self):
        cursor = self.connection.cursor()
        query = "SELECT count(*) FROM vehicules"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_car_insured(self):
        cursor = self.connection.cursor()
        query = """
            SELECT count(*) FROM vehicules
            INNER JOIN quotes ON quotes.id = vehicules.quote_id

            WHERE quotes.insured = 0 and type = 'car'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_moto_insured(self):
        cursor = self.connection.cursor()
        query = """
            SELECT count(*) FROM vehicules
            INNER JOIN quotes ON quotes.id = vehicules.quote_id

            WHERE quotes.insured = 0 and type = 'moto'
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]

    def get_total_vehicules_by_make(self):
        cursor = self.connection.cursor()

        stats = []
        makes = set()
        for _, make, _ in Cars.keys() + Motos.keys():
            makes.add(make)
        for make in makes:

            query = """
                SELECT count(*) FROM vehicules
                INNER JOIN quotes ON quotes.id = vehicules.quote_id

                WHERE vehicules.make = ? AND quotes.insured != 0
            """
            cursor.execute(query, (make,))
            stats.append((make, cursor.fetchone()[0]))

        return stats

    def insert_from_quotes(self, quotes):
        quote_id = self.insert_quote(quotes.quotes[0].driver.gender, quotes.assurable)
        for quote in quotes.quotes:
            if isinstance(quote.vehicule, Car):
                vehicule_type = "car"
            else:
                vechicule_type = "moto"
            self.insert_vehicule(quote_id, quote.vehicule.make, vehicule_type)

    def insert_quote(self, gender, insured):
        cursor = self.connection.cursor()

        query = "INSERT INTO quotes (gender, insured) VALUES(?, ?)"
        cursor.execute(query, (gender, insured))
        self.connection.commit()
        return cursor.lastrowid

    def insert_vehicule(self, quote_id, make, vehicule_type):
        cursor = self.connection.cursor()

        query = "INSERT INTO vehicules (make, quote_id, type) VALUES(?, ?, ?)"
        cursor.execute(query, (make, quote_id, vehicule_type))
        self.connection.commit()
        return cursor.lastrowid

    def return_all_stats(self):
        return {
            "nombre_de_soumissions": self.get_total_quotes(),
            "nombre_de_soumissions_non_assurables":
                self.get_quotes_not_insured(),
            "nombre_de_soumissions_assurables": self.get_quotes_insured(),
            "nombre_de_soumissions_hommes": self.get_quotes_man(),
            "nombre_de_soumissions_femmes": self.get_quotes_woman(),
            "nombre_de_vehicules": self.get_total_vehicules(),
            "nombre_de_voitures_assurables": self.get_total_car_insured(),
            "nombre_de_motos_assurables": self.get_total_moto_insured(),
            "vehicules_par_marques": [
                dict((("marque", r[0]), ("nombre", r[1])))
                    for r in self.get_total_vehicules_by_make()
            ]
        }
