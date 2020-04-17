#!/usr/bin/python3
# -*- coding: Utf-8 -*

from constant1 import *
from classes12 import *



class Product():
	"""
	This class allows us to execute a sql request in order to save product data in a table sql called "product" in mysql.
	"""


	def __init__(self):

		self.msql = MySqlConnector()

		self.product_name = ''
		self.product_nutriscore = ''
		self.product_nutriscore_value = 0
		self.product_url = ''
		self.product_stores = ''
		self.product_category_id = 0
		self.product_category_name = ''


	def add_product(self, product_name, product_nutriscore, product_nutriscore_value, product_url, product_stores, product_category_name, product_category_id):
		""" 
		This method allows us to execute a sql request in order to save product data in a table sql called "product" in mysql.
		"""
		
		self.product_name = product_name
		self.product_nutriscore = product_nutriscore
		self.product_nutriscore_value = product_nutriscore_value
		self.product_url = product_url
		self.product_stores = product_stores
		self.product_category_name = product_category_name
		self.product_category_id = product_category_id

		data_product = (self.product_name, self.product_nutriscore, self.product_nutriscore_value, self.product_url, self.product_stores, self.product_category_name, self.product_category_id) 

		self.msql.request_add_product(data_product)



class Category():
	""" 
	This class allows us to execute a sql request in order to save category data in a table sql called "category" in mysql.
	"""


	def __init__(self):

		self.msql = MySqlConnector()

		self.category_name = ''


	def add_category(self, category_name):
		"""
		This method allows us to execute a sql request in order to save category data in a table sql called "category" in mysql.
		"""

		self.category_name = category_name

		data_category = (self.category_name,)

		self.msql.request_add_category(data_category)

	

class Interface():
	""" 
	This class allows us to generate data for the user interface.
	"""


	def __init__(self, guideline):

		self.msql = MySqlConnector()

		self.i = guideline
		self.proposals = ''
		self.result = ''
		self.list_proposals_categories = ''
		self.list_proposals_products = ''
		self.category_id = ''


	def select_proposal(self, proposals):
		""" 
		This method allows to generate the proposals for the user interface.
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
		This method allows to display the available category for the user interface.
		"""

		self.list_proposals_categories = []
		
		print()
		print('Liste des catégories disponibles:')
		print()
		self.msql.request_search_category()
		print()
		self.result = input(self.i)
		print()

		for row in self.msql.rows1:			
			self.list_proposals_categories.append(str(row[0]))


	def display_product(self, category_id):
		"""
		This method allows to generate the available product for the user interface.
		"""

		self.list_proposals_products = []
		self.category_id = int(category_id)

		print()
		print('Liste des produits issus de la catégorie sélectionnée:')
		print()
		self.msql.request_search_product(self.category_id)
		print()
		self.result = input(self.i)
		print()

		for row in self.msql.rows2:			
			self.list_proposals_products.append(str(row[0]))


	def display_substitute_product(self, category_id):
		"""
		This method allows to generate the available substitute product for the user interface.
		"""

		self.list_proposals_substitute_products = []	
		self.category_id = int(category_id)

		print()
		print('Liste des 5 produits subsituables ayant le meilleur nutriscore:')
		print()
		self.msql.request_search_substitute_product(self.category_id)
		print()
		self.result = input(self.i)
		print()

		for row in self.msql.rows3:			
			self.list_proposals_substitute_products.append(str(row[0]))


	def save_subsitute_product(self, product_id):
		"""
		This method allows to save into the user database, the selected substitute product.
		"""

		self.product_id = int(product_id)

		self.msql.request_save_substitute_product(self.product_id)
		print()
		print('Enregistrement effectué.\nRetrouver votre produit substitué dans votre base de données dans le menu principal.')


	def display_substitued_product(self):
		"""
		This method allows to display the substitued product into the user database.
		"""

		self.list_proposals_substitued_products = []

		print()
		print('Ensemble des vos produits subtitués:')
		print()
		self.msql.request_search_substitued_product()
		print()
		self.result = input(self.i)
		print()

		for row in self.msql.rows4:			
			self.list_proposals_substitued_products.append(str(row[0]))

 	
	def delete_substitued_product(self, product_id):
 		"""
 		This method allows to delete any substitued product into the user database.
 		"""

 		self.product_id = product_id

 		self.msql.request_delete_substitued_product(self.product_id)
 		print()
 		print('Suppression effectuée.\nCe produit ne figurera plus dans votre base de données.')


	def end_process(self):
 		"""
 		This method allows to the user, to quit the program or back to the main menu.
 		"""

 		print()
 		self.result = input(self.i)
