#from quote import Quote
import sqlite3
import os




class bdstats(objet):
	def __init__(self,db_file):

		if os.path.exists(db_file):
			 f = file(db_file)
		else:
			f = file(de_file)  
		self.connection = sqlite3.connect(db_file)

    def create_cursor(self):
        return cursor = self.connection.cursor()

    def create_table(self,cursor):
        cursor.execute('''CREATE TABLE sousmission
                     (id INTEGER PRIMARY KEY, gender TEXT, assurable int,  )''')

        cursor.execute('''create TABLE vehicules (id INTEGER PRIMARY KEY,marque TEXT, soumission INTEGER REFERENCES SOUMISSION (id), type TEXT)''')

    

    def table_commit(self):
        connection.commit()

    def table_close(self,connection):
        connection.close()

