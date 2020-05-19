# Project5_OFF

Project5_OFF : Utilisez les données publiques de l'OpenFoodFacts

Bienvenue !

Projet n°5 du parcours « développeur d’application – Python » chez Openclassrooms. Mise en application du langage Python à travers la réalisation d’un programme utilisant l'API d'OpenFoodFact ainsi que le SGBD MySQL.

Objectif:
Réalisation d'un programme permettant à un utilisateur de rechercher des produits de subsitutions à un panel de produits proposées par catégorie. L'utilisateur aura la possibilité de sauvegarder ses résultats. Il pourra de même visuatiser ses enregistrements et les supprimer si besoin. L'ensemble des données seront issues de l'API d'OpenFoodFact (OFF)


Date de réalisation: mars 2020 - mai 2019 Lien Github: https://github.com/Gontrandddre/Project3_MacGyver

Auteur: Gontrand D., étudiant Openclassrooms.


	1. Comment utiliser ce programme:

Avant toute utilisation de ce programme, il est nécessaire au préalable de:
-créer en local un compte utilisateur MySQL
-remplacer les informations de connexion au sein du fichier 'requests_mysql.py' dans la méthode 'connection' de la classe 'MySQLconector' avec les votre.

Lancement du programme:
L'utilisateur devra se rendre sur le terminal de sa machine et lancer le fichier principal "program.py".

	2. Environnement

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

	3. Structure projet:

-fichiers inspirés du modéle MVC (Modèle Vue Contrôleur):
	- Vue: "interface_program.py";
	- Modèle: "requests_mysql.py" / "create_database.py";
	- Contrôleur: "program.py";
-fichiers supports:
	- Constantes du programme: "constantes.py"
	- Script de la structure de la base de données: "scripts_structure_database.sql"
-fichiers complémentaires: 
	- "requirements.txt" (bibliothèques utilisées);
	- ".gitignore" (dossiers/fichiers à ignorer pour GitHub).

	4. Structure base de données 

Notre programme s'appuie sur le système de gestion de base de données MySql.
Retrouver le modèle physique de données dans le dossier "doc" du répertoire.

	4. Les algorithmes:

- Création de la structure de la base de données:

Ce script permet de créer la structure de la base de données de notre programme. Nous aurons quatre tables:
	- Category;
	- Product;
	- Store;
	- Association;

- Insertion des données dans la base de données: 

	-Category: 10 catégories pré-sélectionnées.
	-Product: 1000 produits par catégorie.
	-Store: Récupération de tous les magasins renseignés par produit.
	-Association: Association d'un produit avec un ou plusieurs magasins. Un produit peut avoir un ou plusieurs magasins, un magasin peut avoir un ou plusieurs produits.


-Gestion de l'interface utilisateur:

A chaque étape du programme, l'utilisateur aura un un guide d'utilisation. En cas d'entrée non valide, le programme proposera à l'utilisateur
A tout moment l'utilisateur peut revenir au menu principal en appuyant sur 'h'
A chaque fin de fonctionnalité, l'utilisateur peut quitter le programme ne appuyant sur 'q'.


Au commencement le programme propose deux fonctinnalités:
1. Rechercher un produit de substitution.
2. Retrouver ses produits substitués

A tout moment l'utilisateur peut revenir au menu principal en appuyant sur 'h'
A chaque fin de fonctionnalité, l'utilisateur peut quitter le programme ne appuyant sur 'q'.

>>>Fonctionnalité 1:
//Affichage des catégories
- Sélectionne une catégorie // Affichage d'un panel de produits.
- Sélectionne un produit // Affichage d'un panel de produits de substitutions.
- Sélectionne un produit de subsitution // Sauvegarde du produit sélectionné.

>>>Fonctionnalité 2:
//Affichage des produits sauvegardés.
- Sélectionne un produit // Suppression du produit sélectionné.

-Gestion des entrées utilisateur:

Le programme vérifie si l'entrée correspond bien à une des propositions affichées.
En cas d'entrée non valide, le programme proposera à l'utilisateur de saisir à nouveau une référence.

	5. Axes de développement:

- Interface graphisme.
- Ajouter sous catégories pour améliorer la recherche d'un produit de substitution.
- Optimiser le code.
- Travailler avec l'ORM SQLAlchemy.
