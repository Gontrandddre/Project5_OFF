#!/usr/bin/python3
# -*- coding: Utf-8 -*


# Category / nutriscore list:

list_category = [['1', 'Biscuits'], ['2', 'Boissons'], ['3', 'Desserts'], ['4', 'Epiceries'], ['5', 'Féculents'], ['6', 'Fromages'], ['7', 'Gateaux'], ['8', 'Légumes'], ['9', 'Poissons'], ['10', 'Viandes']]
list_nutriscore = ['a', 'b', 'c', 'd', 'e']
CONV = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e'} # Pour une meilleure gestion de la recherche d'un S.

# URL OpenFoodFact:

url_begin = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='
url_end = '&sort_by=unique_scans_n&page_size=20&axis_x=energy&axis_y=products_n&action=display&json=1' # page size here............


# Guideline in user interface:

proposals = '1 : Chercher le substitut d\'un aliment.\n2 : Retrouver mes aliments substitués.'
guideline_proposals = 'Sélectionner une des propositions suivantes en rensaignant son ID (1 ou 2).\nPour quitter le programme appuyer sur la touche "q".\nEntrée >>> '
guideline_category = 'Sélectionner une des catégories suivantes en rensaignant son ID.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
guideline_product = 'Sélectionner un des produits suivants en rensaignant son ID, pour avoir les meilleurs substituts.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
guideline_substitute_product = 'Sélectionner un des substituts suivants en rensaignant son ID, pour l\'enregistrer dans votre propore base de données.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
guideline_substitued_product = 'Sélectionner un des aliments subsitutés suivants en renseignant son ID, pour le supprimer de votre base de données.\nPour retourner au menu principal, taper "h".\nEntrée >>> '
guideline_end_process_proposal1 = 'Pour revenir au menu principal, tapez "h".\nPour quitter le programme, tapez "q".\nEntrée >>> '
guideline_end_process_proposal2 = 'Pour revenir au menu principal, tapez "h".\nPour quitter le programme, tapez "q".\nEntrée >>> '

