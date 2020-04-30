# Project5_OFF

Project5_OFF : Utilisez les données publiques de l'OpenFoodFacts

Bienvenue !

Projet n°5 du parcours « développeur d’application – Python » chez Openclassrooms. Mise en application du langage Python à travers la réalisation d’un programme utilisant l'API d'OpenFoodFact ainsi que le SGBD MySQL.


Date de réalisation: mars 2020 - avril 2019 Lien Github: https://github.com/Gontrandddre/Project3_MacGyver

	1. Comment utiliser ce programme:

Avant toute utilisation de ce programme, il est nécessaire de:
-créer en local un compte utilisateur MySQL
-remplacer les informations de connexion au sein du fichier 'classes_mysql.py' dans la méthode 'connection de la classe 'MySQLconector' avec les votre.
-Lancer le programme avec le fichier 'program.py'

	2. Environne & Cahier des charges:

Environnement:

-Langage: Python 3;
-SGBD: MySQL;
-Outil de communication avec la base de données: MySQL-connector;
-Librairie de parsing des données OFF: Request;
-Editeur de teste: SublimeText 3;
-Outil de versionnage: GIT;
-Outils d'audit: Pylint & Flake8;
-Outil de communication: GitHub;
-Solution d'environnement virtuel: VirtualEnv.

Cahier des charges:

Mise en place d'un programme permettant de trouver un substitut à un produit sélectionné par l'utilisateur.
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
	


	3. La structure:

-4 fichiers inspirés du modéle MVC (Modèle Vue Contrôleur): "classes_program.py" & "classes_mysql.py" (caractéristiques des éléments du programme), "constantes.py" (gestion des constantes du programme), "program.py" (logique du programme).
-2 fichiers supports: "requirements.txt" (versions des bibliothèques utilisées, ".gitignore" (dossiers/fichiers à ignorer pour GIT).

	4. Les algorithmes:

- Création des tables: "database.py"

Ce script permet de créer la structure de la base de données de notre programme. Nous aurons quatre tables:
	- Category: Nom des catégories ainsi que leur id.
	- Product: Nom des produits ainsi que leur id, nutriscore, url, etc.
	- Store: Nom des magasins ainsi que leur id.
	- Association: Indique les associations entre id store et id produit.
	- SubstituedProduct: Renseigne les mêmes données que la table 'Product' avec en complément le magasin issu de la table 'Store'.

- Remplissage des tables:

	-Category: Nous insérons dans cette table une liste de 10 catégories choisies au sein de la base de donnée OFF. Générer 1 seul fois au premier lancement du programme.
	-Product: Celle-ci, un emsemble de données issues de l'import des données issues de l'API OFF est inséré.Générer 1 seul fois au premier lancement du programme.
	-Store: De la même manière, les données de cette table correspondent au même import de la table 'Product'.Générer 1 seul fois au premier lancement du programme.
	-Association: Nous insérons ici des données issues de la table 'Product' ainsi que la table 'Store'. Générer 1 seul fois au premier lancement du programme.
	-SubstituedProduct: Cette table est donc vide au premier lancement du programme. Nous insérerons les données issues des tables 'Product' et 'Store' lors de chaque enregistrement d'un produit de substitution par l'utilisateur.

L'ensemble de ces remplissages s'opère via des requetes SQL que l'on retrouve dans le fichier 'classes_mysql.py'.
Nous paramètrons ces requêtes dans le fichier 'classes_program.py' et mettons en application celles-ci dans le fichier principal 'program.py'.


-Gestion de l'interface utilisateur:

Dans ce programme l'utilisateur aura donc accès au terminal. Celui-ci via ce programme proposera plusieurs fonctionnalités, voyons lesquelles:
- Rechercher un produit de substitution.
- Retrouver mes produits substitués


A tout moment l'utilisateur peut revenir au menu principal.
A la fin de chaque fonctionnalité, l'utilisateur à le choix entre quitter le programme et revenir au menu principal.

	Fonctionnalité 1:
Le programme propose dans un premier temps à l'utilisteur de sélectionner une catégorie. Une fois sélectionné, le programme renvoie une liste de produit que l'utilisateur peut substitué en renseignant celui souhaité.
Dès lors, le programme renverra une liste de 5 produits substituables avec le meilleur nutriscore de sa catégorie. En dernier lieu, l'utilisateur choisit d'neregistrer ou non un de ces produits. 
S'il y a enregistrement, le programme intègrera toute les données de ce produit au sein de la table 'SubstituedProduct' qui correspond pour rappel aux enregistrements de l'utilisateur.

	Fonctionnalité 2:
Celle-ci propose à l'utilisateur de visualiser l'ensemble de ses produit enregistrés. Lorsque le programme effectue cette opération, celui-i propose à l'utilisteur s'il en a le souhait de supprimer un des éléments de cette table.


	5. Axes de développement:

- Interface graphisme
- Ajouter sous catégories pour peaufiner le recherche de produit de substitution.
- Optimiser le code
