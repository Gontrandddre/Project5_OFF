#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program constantes.
"""

# Category / nutriscore list:

CATEGORY = {'Biscuits':'1',
            'Boissons':'2',
            'Desserts':'3',
            'Epiceries':'4',
            'Féculents':'5',
            'Fromages':'6',
            'Gateaux':'7',
            'Légumes':'8',
            'Poissons':'9',
            'Viandes':'10'}

CONV = {1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e'}

# URL OpenFoodFact:

URL_BEGIN = 'https://fr.openfoodfacts.org/cgi/search.pl'
P_SIZE = 20

# Info pre data

STEP1 = '\nQue souhaitez-vous faire?\n\
         \n1 : Chercher le substitut d\'un aliment.\
         \n2 : Retrouver mes aliments substitués.'
STEP2 = '\nListe des catégories disponibles:\n\
         \nID : CATEGORIES\n'
STEP3 = '\nListe des produits issus de la catégorie sélectionnée:\n\
         \nID : NOM : NUTRISCORE'
STEP4 = '\nListe des 5 produits subsituables ayant le meilleur nutriscore:\n\
         \nID : NUTRISCORE : URL : MAGASINS'
STEP5 = '\nEnregistrement effectué.\
         \nRetrouver votre produit substitué dans votre base de données dans le menu principal.'
STEP6 = '\nListe de vos produits enregistrés:\n\
         \nID : NAME : NUTRISCORE : URL : CATEGORIE : MAGASINS'
STEP7 = '\nSuppression effectuée.'

# Info post data

STEP1_BIS = '\nSélectionner une des propositions suivantes en rensaignant son ID (1 ou 2).\
             \nPour quitter le programme appuyer sur la touche "q".'
STEP2_BIS = '\nSélectionner une des catégories suivantes en rensaignant son ID.\
             \nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'
STEP3_BIS = '\nPour retrouver les meilleurs substituts d\'un produit, sélectionner son ID.\
             \nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'
STEP4_BIS = '\nPour enregistrer un produit, sélectionner son ID.\
             \nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'
STEP5_BIS = '\nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'
STEP6_BIS = '\nPour supprimer un aliment de votre base de données, sélectionner son ID.\
             \nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'
STEP7_BIS = '\nPour revenir au menu principal, tapez "h".\
             \nPour quitter le programme, tapez "q".'

# Wrong input

WRONG_ID = 'Entrée incorrecte, veuillez réessayer avec le bon ID...'

# Others

NO_RECORD = '(Aucun produit de substitution n\'a été enregistré.)'
END_PROCESS = 'Déconnexion base de données\nFin du programme'

# SQL Requests

REQUEST_ADD_PRODUCT = (""" INSERT INTO Product (name,
                                                nutriscore,
                                                nutriscore_value,
                                                url,
                                                category_name,
                                                category_id)
                           VALUES (%s,
                                   %s,
                                   %s,
                                   %s,
                                   %s,
                                   %s)
                            """)

REQUEST_ADD_CATEGORY = (""" INSERT INTO Category (name)
                            VALUES (%s)
                            """)

REQUEST_ADD_STORE = (""" INSERT INTO Store (name)
                         VALUES (%s)
                            """)

REQUEST_ADD_ASSOCIATION = (""" INSERT INTO Association (product_id,
                                                        store_id)
                               VALUES (%s,
                                       %s)
                               """)

REQUEST_SEARCH_CATEGORY = (""" SELECT id,
                                      name
                               FROM Category
                               """)

REQUEST_SEARCH_STORE = (""" SELECT id,
                                   name
                            FROM Store
                            """)
REQUEST_SEARCH_DATA = (""" SELECT id,
                                  name
                           FROM Product
                           """)

REQUEST_SEARCH_PRODUCT = (""" SELECT id,
                                     name,
                                     nutriscore
                              FROM Product
                              WHERE category_id LIKE %s
                              ORDER BY RAND(id)
                              LIMIT 15
                              """)

REQUEST_SEARCH_SUBSTITUTE_PRODUCT = (""" SELECT p.id,
                                                p.name,
                                                p.nutriscore,
                                                p.url,
                                                GROUP_CONCAT(s.name SEPARATOR ', ') as concat_name
                                         FROM product as p
                                         JOIN association as a
                                         ON p.id = a.product_id
                                         JOIN store as s
                                         ON s.id = a.store_id
                                         WHERE p.category_id LIKE %s
                                         GROUP BY p.id
                                         ORDER BY p.nutriscore
                                         """)

REQUEST_SEARCH_SUBSTITUED_PRODUCT = (""" SELECT p.id,
                                                p.name,
                                                p.nutriscore,
                                                p.url,
                                                p.category_name,
                                                GROUP_CONCAT(s.name SEPARATOR ', ') as concat_name
                                         FROM product as p
                                         JOIN association as a
                                         ON p.id = a.product_id
                                         JOIN store as s
                                         ON s.id = a.store_id
                                         WHERE p.substitut_id IS NOT NULL
                                         GROUP BY p.id
                                         ORDER BY p.substitut_id
                                         """)

REQUEST_SEARCH_PRODUCT_STORES = (""" SELECT MAX(id)
                                     FROM Product
                                     """)

REQUEST_UPDATE_SUBSTITUT_ID = (""" UPDATE Product
                                   SET substitut_id = %s
                                   WHERE id LIKE %s
                                   """)

REQUEST_DELETE_SUBSTITUT_ID = (""" UPDATE Product
                                         SET substitut_id = NULL
                                         WHERE substitut_id LIKE %s
                                         """)
