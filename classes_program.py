#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program classes.
"""

from constantes import (LIST_CATEGORY, RECORD, NO_RECORD, DEL_RECORD)
from classes_mysql import (MySqlConnector)


class Product():
    """
    This class allows us to work with sql request result in order to save product data,
    in a table sql called "product" in mysql with condition.
    """

    def __init__(self):

        self.msql = MySqlConnector()

        self.p_name = ''
        self.p_nutri = ''
        self.p_nutri_value = 0
        self.p_url = ''
        self.p_cat_name = ''
        self.p_cat_id = 0

        self.result_table = ''

    def add_product(self, p_name, p_nutri, p_nutri_value, p_url, p_cat_name, p_cat_id):
        """
        This method allows us to execute a sql request in order to save product data,
        in a table sql called "product" in mysql.
        """

        self.p_name = p_name
        self.p_nutri = p_nutri
        self.p_nutri_value = p_nutri_value
        self.p_url = p_url
        self.p_cat_name = p_cat_name
        self.p_cat_id = p_cat_id

        data_p = (self.p_name,
                  self.p_nutri,
                  self.p_nutri_value,
                  self.p_url,
                  self.p_cat_name,
                  self.p_cat_id)

        self.msql.request_add_product(data_p)

    def condition_load_product(self):
        """
        This method allows us to determinate if the program have to load products from OFF.
        """

        self.msql.request_search_product(LIST_CATEGORY[0][0])
        self.result_table = self.msql.rows3

    def product_id(self):
        """
        This method allows us to find all id in product table.
        """

        self.msql.request_search_product_stores()
        for row in self.msql.rows6:
            return row[0]


class Association():
    """
    This class allows us to work with sql request result in order to save association data,
    in a table sql called "Association" in mysql.
    """

    def __init__(self):

        self.msql = MySqlConnector()

        self.p_id = ''
        self.s_id = ''

    def add_association(self, p_id, s_id):
        """
        This method allows us to execute a sql request in order to save association data,
        in a table sql called "Association" in mysql.
        How many products for a store ? How many stores for a product ? This table determinate it.
        """

        self.p_id = p_id
        self.s_id = s_id

        data_a = (self.p_id, self.s_id)

        self.msql.request_add_association(data_a)


class Category():
    """
    This class allows us to execute a sql request in order to save category data,
    in a table sql called "category" in mysql with condition.
    """

    def __init__(self):

        self.msql = MySqlConnector()

        self.c_name = ''
        self.result_table = ''

    def add_category(self, c_name):
        """
        This method allows us to execute a sql request in order to save category data,
        in a table sql called "category" in mysql.
        """

        self.c_name = c_name

        data_c = (self.c_name,)

        self.msql.request_add_category(data_c)

    def condition_load_category(self):
        """
        This method allows us to determinate if the program have to load categories from OFF.
        """

        self.msql.request_search_category()
        self.result_table = self.msql.rows1


class Store():

    """
    This class allows us to execute a sql request in order to save store data,
    in a table sql called "Store" in mysql with condition.
    """

    def __init__(self):

        self.msql = MySqlConnector()

        self.s_name = ''
        self.result_table = ''

    def add_store(self, s_name):
        """
        This method allows us to execute a sql request in order to save store data,
        in a table sql called "Store" in mysql.
        """

        self.s_name = s_name

        data_s = (self.s_name,)

        self.msql.request_add_store(data_s)

    def condition_load_store(self):
        """
        This method allows us to determinate if the program have to load stores from OFF.
        """

        self.msql.request_search_store()
        self.result_table = self.msql.rows2


class Interface():
    """
    This class allows us to generate data from sql request for the user interface.
    """

    def __init__(self, guideline):

        self.msql = MySqlConnector()

        self.i = guideline
        self.proposals = ''
        self.result = ''

        self.list_proposals_categories = ''
        self.list_proposals_products = ''
        self.list_proposals_substitute_products = ''
        self.list_proposals_substitued_products = ''

        self.c_id = ''
        self.p_id = ''

    def select_proposal(self, proposals):
        """
        This method allows us to generate the proposals for the user interface.
        """

        self.proposals = proposals

        print()
        print('Que voulez-vous faire?')
        print()
        print(self.proposals)
        print()
        self.result = input(self.i)
        print()

    def display_category(self):
        """
        This method allows us to display the available categories for the user interface.
        """

        self.list_proposals_categories = []

        print()
        print('Liste des catégories disponibles:')
        print()
        print('ID : CATEGORIES')
        self.msql.request_search_category()
        for row in self.msql.rows1:
            print('{0} : {1}'.format(row[0], row[1]))
            self.list_proposals_categories.append(str(row[0]))
        print()
        self.result = input(self.i)
        print()

    def display_product(self, c_id):
        """
        This method allows us to generate the available products for the user interface.
        """

        self.list_proposals_products = []
        self.c_id = int(c_id)

        print()
        print('Liste des produits issus de la catégorie sélectionnée:')
        print()
        print('ID : NUTRISCORE : NOM')
        self.msql.request_search_product(self.c_id)
        for row in self.msql.rows3:
            print('{0} : {1} : {2}'.format(row[0], row[2], row[1]))
            self.list_proposals_products.append(str(row[0]))
        print()
        self.result = input(self.i)
        print()

    def display_substitute_product(self, c_id):
        """
        This method allows us to generate the available substitute products for the user interface.
        """

        self.list_proposals_substitute_products = []
        self.c_id = int(c_id)

        print()
        print('Liste des 5 produits subsituables ayant le meilleur nutriscore:')
        print()
        print('ID : NUTRISCORE : URL : MAGASINS')
        self.msql.request_search_substitute_product(self.c_id)
        for row in self.msql.rows4:
            print('{0} : {1} : {2} : {3} : {4}'.format(row[0], row[2], row[1], row[3], row[4]))
            self.list_proposals_substitute_products.append(str(row[0]))
        print()
        self.result = input(self.i)
        print()

    def save_subsitute_product(self, p_id):
        """
        This method allows to save into the user database, the selected substitutes product.
        """

        self.p_id = int(p_id)

        self.msql.request_save_substitute_product(self.p_id)
        print()
        print(RECORD)

    def add_substitut_id(self, p_id):
        """
        This method allows us to save substitut_id,
        in "Product" table from "SubstituedProduct" table.
        """

        self.p_id = int(p_id)

        self.msql.request_add_substitut_id(self.p_id)

    def display_substitued_product(self):
        """
        This method allows us to display,
        the substitued products from the user database.
        """

        self.list_proposals_substitued_products = []

        print()
        print('Ensemble des vos produits subtitués:')
        print()
        print('ID : NOM : NUTRISCORE : URL : MAGASINS')
        self.msql.request_search_substitued_product()
        for row in self.msql.rows5:
            print('{0} : {1} : {2} : {3} : {4} : {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            self.list_proposals_substitued_products.append(str(row[0]))
        if len(self.msql.rows5) == 0:
            print(NO_RECORD)
        print()
        self.result = input(self.i)
        print()

    def delete_substitued_product(self, p_id):
        """
        This method allows us to delete any substitued products,
        into the user database ("SubstituedProduct" table).
        """

        self.p_id = p_id

        self.msql.request_delete_substitued_product(self.p_id)
        print()
        print(DEL_RECORD)

    def end_process(self):
        """
        This method allows us to the user,
        to quit the program or back to the main menu.
        """

        print()
        self.result = input(self.i)
