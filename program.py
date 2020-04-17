#!/usr/bin/python3
# -*- coding: Utf-8 -*

import sys
import requests

from database1 import *
from constant1 import *
from classes1 import *



class Program():
	"""
	This class allows us to generate data from OpennFoodFactin our database "category" and "product".
	Then, we create an interface for the user, he can search a substitute product to save it, 
	or find his saved substitued product from his database.

	"""


	def __init__(self):
		
		self.category = Category()
		self.product = Product()

		self.display_proposals = Interface(guideline_proposals)
		self.display_category = Interface(guideline_category)
		self.display_product = Interface(guideline_product)
		self.display_substitute_product = Interface(guideline_substitute_product)
		self.save_substitute_product = Interface(guideline='')
		self.end_process_proposal1 = Interface(guideline_end_process_proposal1)
		self.end_process_proposal2 = Interface(guideline_end_process_proposal2)

		self.display_substitued_product = Interface(guideline_substitued_product)
		self.delete_substitued_product = Interface(guideline='')

			
	def  generate_data_category(self):
		""" 
		This method allows to insert the categories into our table sql 'category'.
		We select 10 categories from OpenFoodFact.
		"""

		category_name = ''

		for a, b in list_category:

			category_name = b

			self.category.add_category(category_name)


	def generate_data_product(self):
		""" 
		This method allows to insert data of product from OpenFoodFact into our table 'product'.
		We select 10 products per category.
		"""

		product_name = ''
		product_nutriscore = ''
		product_nutriscore_value = ''
		product_category_name = ''
		product_url = ''
		product_category_id = ''
		product_stores = ''

		print('Chargement des données')

		for a, b in list_category:

			url = "{}{}{}".format(url_begin, b, url_end)
				
			response = requests.get(url)
			response_json = response.json()

			for p in response_json["products"]:

				try:
					product_name = p["product_name_fr"]
					product_nutriscore = p["nutriscore_grade"]
					product_category_name = b
					product_url = p["url"]            
					product_category_id = a
					product_stores = p["stores"]

					for x, y in CONV.items():
						if product_nutriscore == y:
							product_nutriscore_value = x

					self.product.add_product(product_name, product_nutriscore, product_nutriscore_value, product_url, product_stores, product_category_name, product_category_id)

				except KeyError:
					pass


	def interface(self):
		""" 
		This method allows us to create an interface between our table SQL (category and product) and the user.
		During this loop, the user will be able to find his substitued product or save subsitute products.
		To save substitute product, the user will have to select an category and a product to find a substitute product.
		"""

		self.display_proposals.select_proposal(proposals)
		result1 = self.display_proposals.result

		while result1 != '1' and result1 != '2' and result1 != 'h' and result1 != 'q':
			a = input('Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> ')
			result1 = a

		else:
			if result1 == '1':
				self.display_category.display_category()
				result2 = self.display_category.result

				while result2 not in self.display_category.list_proposals_categories and result2 != 'h':
					a = input('Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> ')
					result2 = a

				else:
					if result2 in self.display_category.list_proposals_categories:
						self.display_product.display_product(result2)
						result3 = self.display_product.result

						while result3 not in self.display_product.list_proposals_products and result3 != 'h':
							a = input('Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> ')
							result3 = a

						else:
							if result2 in self.display_category.list_proposals_categories and result3 != 'h':
								self.display_substitute_product.display_substitute_product(result2)
								result4 = self.display_substitute_product.result

								while result4 not in self.display_substitute_product.list_proposals_substitute_products and result4 != 'h':
									a = input('Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> ')
									result4 = a

								else:
									if result4 in self.display_substitute_product.list_proposals_substitute_products:
										self.save_substitute_product.save_subsitute_product(result4)
										self.end_process_proposal1.end_process()

										result5 = self.end_process_proposal1.result

										while result5 != 'q' and result5 != 'h':
											a = input('Mauvaise entrée, veuillez réessayer ("q" pour quitter / "h" pour revenir au menu principal)...\nEntrée >>> ')
											result5 = a

										else:
											if result5 == 'q':
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
					a = input('Mauvaise entrée, veuillez réessayer avec le bon ID...\nEntrée >>> ')
					result2 = a

				else:
					if result2 in self.display_substitued_product.list_proposals_substitued_products:
						self.delete_substitued_product.delete_substitued_product(result2)
						self.end_process_proposal2.end_process()

						result3 = self.end_process_proposal2.result

						while result3 != 'q' and result3 != 'h':
								a = input('Mauvaise entrée, veuillez réessayer ("q" pour quitter / "h" pour revenir au menu principal)...\nEntrée >>> ')
								result3 = a

						else:
							if result3 == 'q':
									sys.exit()

							elif result3 == 'h':
								back_home = Program()
								back_home.interface()

					elif result2 == 'h':
						back_home = Program()
						back_home.interface()

			elif result1 == 'q':
				sys.exit()



program = Program()
program.generate_data_category()
program.generate_data_product()
program.interface()
