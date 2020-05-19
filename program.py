#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
You must follow instructions into interface user.
Main file: program.py
Files : program.py, classes_program.py, classes_mysql.py, constantes.py, database.py.
"""

import sys
import requests

from create_database import (Table)
from constantes import (
    CATEGORY, CONV, URL_BEGIN, P_SIZE,
    STEP1, STEP1_BIS,
    STEP2, STEP2_BIS,
    STEP3, STEP3_BIS,
    STEP4, STEP4_BIS,
    STEP5, STEP5_BIS,
    STEP6, STEP6_BIS,
    STEP7, STEP7_BIS,
    WRONG_ID, END_PROCESS,
    REQUEST_ADD_PRODUCT, REQUEST_ADD_CATEGORY, REQUEST_ADD_ASSOCIATION, REQUEST_ADD_STORE,
    REQUEST_SEARCH_CATEGORY, REQUEST_SEARCH_STORE, REQUEST_SEARCH_PRODUCT,
    REQUEST_SEARCH_SUBSTITUTE_PRODUCT, REQUEST_SEARCH_SUBSTITUED_PRODUCT,
    REQUEST_SEARCH_PRODUCT_STORES, REQUEST_UPDATE_SUBSTITUT_ID,
    REQUEST_DELETE_SUBSTITUT_ID, REQUEST_SEARCH_DATA
)
from interface_program import (Interface)
from requests_mysql import (MySqlConnector)


class Data():
    """
    This class allows us to work with sql request result in order to insert product data,
    in a table sql called "product" in mysql with condition.
    """

    def __init__(self, **attributes):

        self.mysql = MySqlConnector()

        for attr_name, attr_value in attributes.items():
            setattr(self, attr_name, attr_value)

    def add_data(self, request, **attributes):
        """
        This method allows us to execute a sql request in order to insert product data,
        in a table sql called "product" in mysql.
        """

        liste = []

        for attr_name, attr_value in attributes.items():
            if attr_name != 'mysql':
                attributes[attr_name] = attr_value
                liste.append(attributes[attr_name])

        self.mysql.request_add_data(request, tuple(liste))

    def condition_load_data(self, request):
        """
        This method allows us to determinate if the program have to load products from OFF.
        """
        return self.mysql.request_searchall_data(request)

    def product_id(self, request):
        """
        This method allows us to find all id in product table.
        """

        self.mysql.request_searchall_data(request)
        for row in self.mysql.rows:
            return row[0]


class Program():
    """
    This class allows us to generate data from OpenFoodFact in our database "category" & "product".
    Then, we create an interface for the user, he can search a substitute product to save it,
    or find his saved substitued product.
    """

    def __init__(self):

        self.page_size = P_SIZE

        self.product = ''
        self.category = ''
        self.store = ''
        self.association = ''

        self.table = Table()
        self.table.generate_structure_database("script_structure_database.sql")

        self.mysql = MySqlConnector()
        self.mysql.connection()

        self.display_proposals = Interface()
        self.display_c = Interface()
        self.display_p = Interface()
        self.display_sub_p = Interface()
        self.display_save_p = Interface()

        self.display_saved_p = Interface()
        self.display_delete_p = Interface()

    def generate_data(self):
        """
        This method allows us to generate data program into mysql database.
        """

        self.product = Data(**{'p_name':'',
                               'p_nutri':'',
                               'p_nutri_value':'',
                               'p_url':'',
                               'p_cat_name':'',
                               'p_cat_id':''})

        self.category = Data(**{'c_name':''})

        self.store = Data(**{'s_name':''})

        self.association = Data(**{'p_id':'',
                                   's_id':''})

        if self.product.condition_load_data(REQUEST_SEARCH_DATA) == []:

            print('Chargement des données d\'OpenFoodFact en-cours...')
            self.generate_category()
            self.generate_store()
            self.generate_product()
            print('Chargement des données d\'OpenFoodFact finalisé.')

        else:
            print('Les données d\'OpenFoddFact ont déjà été téléchargé.')

    def generate_category(self):
        """
        This method allows us to pick category data,
        and insert into mysql database.
        We pre-determinate 10 categories from OpenFoodFact.
        """

        for cat_name in CATEGORY:

            try:
                self.category.c_name = cat_name

                self.category.add_data(REQUEST_ADD_CATEGORY, **self.category.__dict__)

            except KeyError:
                pass

    def generate_store(self):
        """
        This method allows us to extract stores from OpenFoodFact API,
        and insert stores data into table 'Store' from mysql database.
        """

        liste_stores_brut = []
        liste_stores = []

        for cat_name in CATEGORY:

            params_url = {'action':'process',
                          'tagtype_0':'categories',
                          'tag_contains_0':'contains',
                          'tag_0':cat_name,
                          'sort_by':'unique_scans_n',
                          'page_size':self.page_size,
                          'axis_x':'energy',
                          'axis_y':'products_n',
                          'json':'1'}
            response = requests.get(URL_BEGIN, params=params_url)
            response_json = response.json()

            for product in response_json["products"]:

                try:
                    self.store.s_name = product["stores"]

                    stores_product = self.store.s_name.split(",")
                    liste_stores_brut.extend(stores_product)
                    liste_stores = list(set(liste_stores_brut))
                except KeyError:
                    pass

        for store in liste_stores:
            self.store.s_name = store
            self.store.add_data(REQUEST_ADD_STORE, **self.store.__dict__)

    def generate_product(self):
        """
        This method allows us to extract products from OpenFoodFact API,
        and insert products data into table 'Product' from mysql database.
        """

        for cat_name, cat_id in CATEGORY.items():

            params_url = {'action':'process',
                          'tagtype_0':'categories',
                          'tag_contains_0':'contains',
                          'tag_0':cat_name,
                          'sort_by':'unique_scans_n',
                          'page_size':self.page_size,
                          'axis_x':'energy',
                          'axis_y':'products_n',
                          'json':'1'}
            response = requests.get(URL_BEGIN, params=params_url)
            response_json = response.json()

            for product in response_json["products"]:

                try:
                    self.product.p_name = product["product_name_fr"]
                    self.product.p_nutri = product["nutriscore_grade"]
                    self.product.p_url = product["url"]
                    self.product.p_cat_name = cat_name
                    self.product.p_cat_id = cat_id

                    for n_id, n_text in CONV.items():
                        if self.product.p_nutri == n_text:
                            self.product.p_nutri_value = n_id

                    self.product.add_data(REQUEST_ADD_PRODUCT, **self.product.__dict__)

                    list_stores_per_product = product['stores'].split(",")
                    self.store.condition_load_data(REQUEST_SEARCH_STORE)
                    for row in self.store.condition_load_data(REQUEST_SEARCH_STORE):
                        for store in list_stores_per_product:
                            if row[1] == store:
                                self.association.p_id = \
                                    self.product.product_id(REQUEST_SEARCH_PRODUCT_STORES)
                                self.association.s_id = row[0]
                                self.association.add_data(REQUEST_ADD_ASSOCIATION,
                                                          **self.association.__dict__)

                except KeyError:
                    pass

    def main(self):
        """
        This method allows us to start the program.
        At the beginning, the user have to select one of these proposals.
        """

        self.display_proposals.display(STEP1, STEP1_BIS)
        proposal = self.get_input(['1', '2'])

        if proposal == '1':
            self.process_find_substitute_product()

        elif proposal == '2':
            self.process_display_saved_product()

    def get_input(self, list_valid_input):
        """
        This method allows us to manage user input from user interface.
        At each steps:
        - The user can leave the programm.
        - The user can return back in the main menu.
        """

        ret = input('Entrée >>> ')

        while ret not in list_valid_input:

            if ret == 'h':
                back_home = Program()
                back_home.main()

            elif ret == 'q':
                self.mysql.cursor.close()
                print(END_PROCESS)
                sys.exit()

            else:
                ret = input(WRONG_ID)

        return ret

    def process_find_substitute_product(self):
        """
        This method allows us to start the first functionality of the program.
        At the end of the process:
        - The user find substitue product.
        - The user can save a substitute product.
        """

        ################################################ Display Category
        data_c = self.mysql.request_searchall_data(REQUEST_SEARCH_CATEGORY)

        self.display_c.display(STEP2, STEP2_BIS, request=data_c)

        ################################################ Display Product
        step3_attributes = (int(self.get_input(self.display_c.list_valid_input)),)

        data_p = self.mysql.request_searchmany_data(REQUEST_SEARCH_PRODUCT,
                                                    step3_attributes, many=15)

        self.display_p.display(STEP3, STEP3_BIS, request=data_p)

        ################################################ Display Substitute Product
        self.get_input(self.display_p.list_valid_input)

        data_sub_p = self.mysql.request_searchmany_data(REQUEST_SEARCH_SUBSTITUTE_PRODUCT,
                                                        step3_attributes, many=5)

        self.display_sub_p.display(STEP4, STEP4_BIS, request=data_sub_p)

        ################################################ Save Substitute Product
        attribute = int(self.get_input(self.display_sub_p.list_valid_input))
        step5_attributes = (attribute, attribute)

        self.mysql.request_update_data(REQUEST_UPDATE_SUBSTITUT_ID,
                                       step5_attributes)

        self.display_save_p.display(STEP5, STEP5_BIS, display_result='No')

        ################################################ End process1
        self.get_input(self.display_save_p.list_valid_input)

    def process_display_saved_product(self):
        """
        This method allows us to start the second functionality of the program.
        At the end of the process:
        - The user refind saved products.
        - The user can delete a saved product.
        """

        ################################################ Display Substitued Product
        data_saved_p = self.mysql.request_searchall_data(REQUEST_SEARCH_SUBSTITUED_PRODUCT)

        self.display_saved_p.display(STEP6, STEP6_BIS, request=data_saved_p)

        ################################################ Delete Substituted Product
        step7_attributes = (int(self.get_input(self.display_saved_p.list_valid_input)),)

        self.mysql.request_update_data(REQUEST_DELETE_SUBSTITUT_ID,
                                       step7_attributes)

        self.display_delete_p.display(STEP7, STEP7_BIS, display_result='No')

        ################################################ End process2
        self.get_input(self.display_delete_p.list_valid_input)


if __name__ == "__main__":

    program = Program()
    program.generate_data()
    program.main()
