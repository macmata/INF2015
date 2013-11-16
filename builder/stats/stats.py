from quote import Quote
import sqlite3






conn = sqlite3.connect('statistiques.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stats
		             (homme INETEGER, femme INTERGER, nbVoiture INTERGER, nbMotos INTERGER, nbVoitures INTERGER,)''')

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()



"nb soumision"
"nb soumission non assurable"
"qte homme"
"qte femme"
"nb vehicule"
"nb voiture"
"nb moto"
"vehicule par marque"


