NF2015 – Développement de logiciels dans un environnement Agile

Projet de session – Automne 2013

Demande initiale

Notre client nous demande de lui livrer ces fonctionnalités pour le 9 octobre 2013, avant 9h30. La 

date de livraison n'est pas négociable.

L'application à développer est un logiciel qui calculera des demandes de soumission d'assurance 

automobile pour des voitures de luxe.

Dans le domaine des assurances, il existe beaucoup de clauses, de cas d'exceptions et de 

particularités avec les contrats d'assurance, et les contrats de notre client ne font pas exception. Il a 

donc besoin d'un coup de main pour l'aider à se retrouver dans toutes ses règles afin d'assurer une 

croissance à son entreprise.

Le logiciel ne possèdera pas d'interface utilisateur car il est destiné à être invoqué à partir d'une 

application web. Le contrat ne consiste donc qu'au développement du "back-end" de l'application.

Fonctionnalités

Le fichier d'entrée, en format JSON, aura l'air de ceci :

{

 "voiture": {

 "annee": 2014,

 "marque": "Porsche",

 "modele": "911 Turbo S",

 "valeur_des_options": 8000.00,

 "burinage": "PROACTIF",

 "garage_interieur": true,

 "systeme_alarme": false

 },

 "conducteur": {

 "date_de_naissance": "1977-01-15",

 "province": "Québec",

 "ville": "Montréal",

 "sexe": "M",

 "date_fin_cours_de_conduite": "2000-12-01",

 "cours_de_conduite_reconnus_par_CAA": true,

 "premier_contrat": false

 },

 "duree_contrat": 2

}

Le fichier de résultat généré par le logiciel devra ressembler à ceci :

{

 "assurable": true,

 "montant_annuel": 8437.34,

 "mensualite": 713.66

}
