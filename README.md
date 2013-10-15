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


[On retire 1000$ au montant de l'assurance si le conducteur est une femme.]
[On ajoute 1000$ au montant de l'assurance si le conducteur est un homme de moins de 35 ]



le montant de base n'est plus nécessairement 9% de la valeur initiale du véhicule et change pour :
homme
Âge Pourcentage
25 à 35 ans 15%
36 à 60 ans 12%
61 à 75 ans 13.5%
femme
Âge Pourcentage
21 à 40 ans 11%
41 à 65 ans 9%
66 à 75 ans 15.5%

>
Il doit être possible d'assurer plusieurs véhicules sur un même contrat d'assurance
la propriété "voiture" deviendra "voitures" et sa valeur sera un tableau de voitures. 
Le montant total du contrat d'assurance sera la somme du montant d'assurance de chaque voiture 

>
Par exemple, si c'est le premier contract d'assurance d'une personne et qu'il assure trois 
voitures, il devrait payer trois fois la pénalité de 2000$.

Pour toutes les voitures valant plus de 500 000$, on doit payer une taxe supplémentaire de 2 500$, 
ajouté au montant de la soumission.


#Rabais ingenieur

Notre client offre 10% de rabais supplémentaire sur tous les contrats d'assurance pour les membres 

##Motos
de l'Ordre des ingénieurs du Québec. Dans l'objet "conducteur", une nouvelle propriété booléenne 
nommée "membre_oiq" indiquera s'il s'agit d'un membre de l'Ordre ou non.
