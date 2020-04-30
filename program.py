#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
You must follow instructions into interface user.
Main file: program.py
Files : program.py, classes_program.py, classes_mysql.py, constantes.py, database.py.
"""

import sys
import requests

from database import (Database)
from constantes import (
        LIST_CATEGORY, CONV, URL_BEGIN, URL_END, PROPOSALS,
        GUIDELINE_PROPOSALS, GUIDELINE_CATEGORY, GUIDELINE_PRODUCT,
        GUIDELINE_SUBSTITUTE_PRODUCT, GUIDELINE_SUBSTITUED_PRODUCT,
        GUIDELINE_END_PROCESS_PROPOSAL1, GUIDELINE_END_PROCESS_PROPOSAL2,
        WRONG_ID, WRONG_INPUT, END_PROCESS
)
from classes_program import (Product, Association, Category, Store, Interface)
from classes_mysql import (MySqlConnector)


class Program():
    """
    This class allows us to generate data from OpenFoodFact in our database "category" & "product".
    Then, we create an interface for the user, he can search a substitute product to save it,
    or find his saved substitued product from his database.
    """

    def __init__(self):

        self.table = Database()
        self.table.table()

        self.category = Category()
        self.product = Product()
        self.store = Store()
        self.association = Association()

        self.display_proposals = Interface(GUIDELINE_PROPOSALS)
        self.display_category = Interface(GUIDELINE_CATEGORY)
        self.display_product = Interface(GUIDELINE_PRODUCT)
        self.display_substitute_product = Interface(GUIDELINE_SUBSTITUTE_PRODUCT)
        self.save_substitute_product = Interface(guideline='')
        self.add_substitut_id = Interface(guideline='')
        self.end_process_proposal1 = Interface(GUIDELINE_END_PROCESS_PROPOSAL1)
        self.end_process_proposal2 = Interface(GUIDELINE_END_PROCESS_PROPOSAL2)

        self.display_substitued_product = Interface(GUIDELINE_SUBSTITUED_PRODUCT)
        self.delete_substitued_product = Interface(guideline='')

        self.disconnect_mysql = MySqlConnector()
        self.disconnect_mysql.connection()

    def generate_data_category(self):
        """
        This method allows to insert the categories into our table sql 'Category'.
        We select 10 categories from OpenFoodFact.
        """

        self.category.condition_load_category()

        if self.category.result_table == []:

            self.table.foreign_key()

            c_name = ''

            print('Chargement des catégories en-cours...')

            for cat_id, cat_name in LIST_CATEGORY:

                c_name = cat_name

                self.category.add_category(c_name)

            print('Chargement des catégories finalisé.')

        else:
            print('Les catégories ont déjà été téléchargé.')

    def generate_data_store(self):
        """
        This method allows to insert the stores into our table sql 'Store'.
        """

        liste_stores_brut = []
        liste_stores = []

        self.store.condition_load_store()

        if self.store.result_table == []:

            s_name = ''

            print('Chargement des magasins en-cours...')

            for cat_id, cat_name in LIST_CATEGORY:

                url = "{}{}{}".format(URL_BEGIN, cat_name, URL_END)

                response = requests.get(url)
                response_json = response.json()

                for product in response_json["products"]:

                    try:
                        s_name = product["stores"]

                        stores_product = s_name.split(",")
                        liste_stores_brut.extend(stores_product)
                        liste_stores = list(set(liste_stores_brut))

                    except KeyError:
                        pass

            for store in liste_stores:

                self.store.add_store(store)

            print('Chargement des magasins finalisé.')

        else:
            print('Les magasins ont déjà été téléchargé.')

    def generate_data_product(self):
        """
        This method allows to insert the categories into our table sql 'Category'.
        We select 1000 products per category from OpenFoodFact.
        """

        self.product.condition_load_product()

        if self.product.result_table == []:

            p_name = ''
            p_nutri = ''
            p_nutri_value = ''
            p_url = ''
            p_stores = ''
            p_cat_name = ''
            p_cat_id = ''

            print('Chargement des données d\'OpenFoodFact en-cours...')

            for cat_id, cat_name in LIST_CATEGORY:

                url = "{}{}{}".format(URL_BEGIN, cat_name, URL_END)

                response = requests.get(url)
                response_json = response.json()

                for product in response_json["products"]:

                    try:
                        p_name = product["product_name_fr"]
                        p_nutri = product["nutriscore_grade"]
                        p_url = product["url"]
                        p_stores = product["stores"]
                        p_cat_name = cat_name
                        p_cat_id = cat_id

                        for n_id, n_text in CONV.items():
                            if p_nutri == n_text:
                                p_nutri_value = n_id

                        self.product.add_product(p_name, p_nutri, p_nutri_value, p_url, p_cat_name, p_cat_id)
                        print(p_name, p_nutri, p_nutri_value, p_url, p_cat_name, p_cat_id)

                    except KeyError:
                        pass

                    except ValueError:
                        pass

                    try:
                        liste_product_stores = p_stores.split(",")
                        p_id = self.product.product_id()

                        self.store.condition_load_store()
                        for row in self.store.result_table:

                            for store in liste_product_stores:
                                if row[1] == store:
                                    self.association.add_association(p_id, row[0])

                    except KeyError:
                        pass

            print('Chargement des données d\'OpenFoodFact finalisé.')

        else:
            print('Les données d\'OpenFoddFact ont déjà été téléchargé.')

    def interface(self):
        """
        This method allows us to create an interface between our tables SQL and the user.
        During this loop,
        the user will be able to find his substitued product or save subsitute products.
        To save substitute product,
        the user will have to select an category and a product to find a substitute product.
        """

        self.display_proposals.select_proposal(PROPOSALS)
        result1 = self.display_proposals.result

        while result1 not in ('1', '2', 'h', 'q'):
            result_bis = input(WRONG_ID)
            result1 = result_bis
            break

        else:
            if result1 == '1':
                self.display_category.display_category()
                result2 = self.display_category.result

                while result2 not in self.display_category.list_proposals_categories and result2 != 'h':
                    result_bis = input(WRONG_ID)
                    result2 = result_bis
                    break

                else:
                    if result2 in self.display_category.list_proposals_categories:
                        self.display_product.display_product(result2)
                        result3 = self.display_product.result

                        while result3 not in self.display_product.list_proposals_products and result3 != 'h':
                            result_bis = input(WRONG_ID)
                            result3 = result_bis
                            break

                        else:
                            if result2 in self.display_category.list_proposals_categories and result3 != 'h':
                                self.display_substitute_product.display_substitute_product(result2)
                                result4 = self.display_substitute_product.result

                                while result4 not in self.display_substitute_product.list_proposals_substitute_products and result4 != 'h':
                                    result_bis = input(WRONG_ID)
                                    result4 = result_bis
                                    break

                                else:
                                    if result4 in self.display_substitute_product.list_proposals_substitute_products:
                                        self.save_substitute_product.save_subsitute_product(result4)
                                        self.add_substitut_id.add_substitut_id(result4)
                                        self.end_process_proposal1.end_process()

                                        result5 = self.end_process_proposal1.result

                                        while result5 not in ('q', 'h'):
                                            result_bis = input(WRONG_INPUT)
                                            result5 = result_bis
                                            break

                                        else:
                                            if result5 == 'q':
                                                self.disconnect_mysql.cursor.close()
                                                print(END_PROCESS)
                                                sys.exit()

                                            elif result5 == 'h':
                                                back_home = Program()
                                                back_home.interface()

                                    elif result4 == 'h':
                                        back_home = Program()
                                        back_home.interface()

                            elif result3 == 'h':
                                back_home = Program()
                                back_home.interface()

                    elif result2 == 'h':
                        back_home = Program()
                        back_home.interface()

            elif result1 == '2':
                self.display_substitued_product.display_substitued_product()
                result2 = self.display_substitued_product.result

                while result2 not in self.display_substitued_product.list_proposals_substitued_products and result2 != 'h':
                    result_bis = input(WRONG_ID)
                    result2 = result_bis
                    break

                else:
                    if result2 in self.display_substitued_product.list_proposals_substitued_products:
                        self.delete_substitued_product.delete_substitued_product(result2)
                        self.end_process_proposal2.end_process()

                        result3 = self.end_process_proposal2.result

                        while result3 not in ('q', 'h'):
                            result_bis = input(WRONG_INPUT)
                            result3 = result_bis
                            break

                        else:
                            if result3 == 'q':
                                self.disconnect_mysql.cursor.close()
                                print(END_PROCESS)
                                sys.exit()

                            elif result3 == 'h':
                                back_home = Program()
                                back_home.interface()

                    elif result2 == 'h':
                        back_home = Program()
                        back_home.interface()

            elif result1 == 'q':
                self.disconnect_mysql.cursor.close()
                print(END_PROCESS)
                sys.exit()


PROGRAM = Program()
PROGRAM.generate_data_category()
PROGRAM.generate_data_store()
PROGRAM.generate_data_product()
PROGRAM.interface()
