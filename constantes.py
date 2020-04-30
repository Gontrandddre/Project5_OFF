#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program constantes.
"""

# Category / nutriscore list:

LIST_CATEGORY = [['1', 'Biscuits'],
                 ['2', 'Boissons'],
                 ['3', 'Desserts'],
                 ['4', 'Epiceries'],
                 ['5', 'Féculents'],
                 ['6', 'Fromages'],
                 ['7', 'Gateaux'],
                 ['8', 'Légumes'],
                 ['9', 'Poissons'],
                 ['10', 'Viandes']]

LIST_NUTRISCORE = ['a', 'b', 'c', 'd', 'e']

CONV = {1 : 'a',
        2 : 'b',
        3 : 'c',
        4 : 'd',
        5 : 'e'}

# URL OpenFoodFact:

URL_BEGIN = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='
URL_END = '&sort_by=unique_scans_n&page_size=200&axis_x=energy&axis_y=products_n&action=display&json=1' # page_size = number of product per url...


# Guideline in user interface:

PROPOSALS = '1 : Chercher le substitut d\'un aliment.\n2 : Retrouver mes aliments substitués.'
GUIDELINE_PROPOSALS = 'Sélectionner une des propositions suivantes en rensaignant son ID (1 ou 2).\nPour quitter le programme appuyer sur la touche "q".\nEntrée >>> '
GUIDELINE_CATEGORY = 'Sélectionner une des catégories suivantes en rensaignant son ID.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
GUIDELINE_PRODUCT = 'Sélectionner un des produits suivants en rensaignant son ID, pour avoir les meilleurs substituts.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
GUIDELINE_SUBSTITUTE_PRODUCT = 'Sélectionner un des substituts suivants en rensaignant son ID, pour l\'enregistrer dans votre propore base de données.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
GUIDELINE_SUBSTITUED_PRODUCT = 'Sélectionner un des aliments subsitutés suivants en renseignant son ID, pour le supprimer de votre base de données.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
GUIDELINE_END_PROCESS_PROPOSAL1 = 'Pour revenir au menu principal, tapez "h".\nPour quitter le programme, tapez "q".\nEntrée >>> '
GUIDELINE_END_PROCESS_PROPOSAL2 = 'Pour revenir au menu principal, tapez "h".\nPour quitter le programme, tapez "q".\nEntrée >>> '

# Wrong input

WRONG_ID = 'Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> '
WRONG_INPUT = 'Mauvaise entrée, veuillez réessayer ("q" pour quitter / "h" pour revenir au menu principal)...\nEntrée >>> '

# Others

RECORD = 'Enregistrement effectué.\nRetrouver votre produit substitué dans votre base de données dans le menu principal.'
NO_RECORD = '(Aucun produit de substitution n\'a été enregistré.)'
DEL_RECORD = 'Suppression effectuée.\nCe produit ne figurera plus dans votre base de données.'
END_PROCESS = 'Déconnexion base de données\nFin du programme'
