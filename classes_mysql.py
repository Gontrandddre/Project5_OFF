#!/usr/bin/python3
# -*- coding: Utf-8 -*

import mysql.connector
from mysql.connector import errorcode



class MySqlConnector():
	"""
	This class allows us to create request SQL and to connect on mysql. 
	"""


	def __init__(self):

		self.r_add_product = ''
		self.r_add_category = ''

		self.r_display_category = ''
		self.r_display_product = ''
		self.r_display_substitute_product = ''
		self.r_display_substitued_product = ''

		self.rows1 = ''

		try:
			self.conn = mysql.connector.connect(host='localhost', user='user_p5', password='iutgea', database='p5') # connection to mysql.

		except mysql.connector.Error as err:

			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with the user name or password")

			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print('Database does not exist')

			else:
				print(err)

		else:
			self.cursor = self.conn.cursor(buffered=True)


	def request_add_product(self, data_product):
		"""
		This method allows to create a request SQL wich will insert the data product from OpenFoodFact into our database mysql.
		"""

		self.data_product = data_product

		self.r_add_product = ("""INSERT INTO product (name, nutriscore, nutriscore_value, url, stores, category_name, category_id) 
								 VALUES (%s, %s, %s, %s, %s, %s, %s) """)
		self.cursor.execute(self.r_add_product, self.data_product)
		self.conn.commit()


	def request_add_category(self, data_category):
		"""
		This method allows to create a request SQL wich will insert the data category into our database mysql.
		"""
		self.data_category = data_category

		self.r_add_category = (""" INSERT INTO category (name) 
								   VALUES (%s) """)
		self.cursor.execute(self.r_add_category, self.data_category)
		self.conn.commit()


	def request_search_category(self):
		"""
		This method allows to create a request SQL wich will search data category in our database "category".
		"""

		self.r_search_category = (""" SELECT id, name 
									  FROM category """)
		self.cursor.execute(self.r_search_category)
		self.rows1 = self.cursor.fetchall()
		self.conn.commit()
		for row in self.rows1:
			print('{0} : {1}'.format(row[0], row[1]))


	def request_search_product(self, category_id):
		"""
		This method allows to create a request SQL wich will search data product in our database "product".
		"""

		self.category_id = category_id

		self.r_search_product = (""" SELECT id, name, nutriscore 
									 FROM product 
									 WHERE category_id LIKE %s """)
		self.cursor.execute(self.r_search_product, (self.category_id,))
		self.rows2 = self.cursor.fetchall()
		self.conn.commit()
		for row in self.rows2:
			print('{0} : {1} : {2}'.format(row[0], row[2], row[1]))


	def request_search_substitute_product(self, category_id):
		"""
		This method allows to create a request SQL wich will search substitute product in our database "product".
		For that, we collect the best of 5 nutriscore in the same category to find a substitute product.
		"""

		self.category_id = category_id

		self.r_search_substitute_product = (""" SELECT id, name, nutriscore, url, stores 
												FROM product 
												WHERE category_id LIKE %s 
												ORDER BY nutriscore """) 
		self.cursor.execute(self.r_search_substitute_product, (self.category_id,)) # A FAIRE
		self.rows3 = self.cursor.fetchmany(5)
		self.conn.commit()
		for row in self.rows3:
			print('{0} : {1} : {2} : {3}'.format(row[0], row[2], row[1], row[3]))


	def request_save_substitute_product(self, product_id):
		"""
		This method allows us to create a request SQL to insert on our database "substitued_product" the data from the substitute product selected by the user.
		"""
		
		self.product_id = product_id

		self.r_save_product = (""" INSERT INTO substitued_product(name, nutriscore, nutriscore_value, url, stores, category_name, category_id) 
								   SELECT name, nutriscore, nutriscore_value, url, stores, category_name, category_id
								   FROM product
								   WHERE id LIKE %s""")

		self.cursor.execute(self.r_save_product, (self.product_id,)) 
		self.conn.commit()


	def request_search_substitued_product(self):
		"""
		This method allows us to create a request SQL wich will select the data from the substitued_product database (user database).
		"""

		self.r_search_substitued_product = (""" SELECT DISTINCT id, name, nutriscore, category_name, url, stores
												FROM substitued_product """)
		self.cursor.execute(self.r_search_substitued_product)
		self.conn.commit()
		self.rows4 = self.cursor.fetchall()
		for row in self.rows4:
			print('{0} : {1} : {2} : {3} : {4} : {5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))


	def request_delete_substitued_product(self, product_id):
		"""
		This method allows us to create a request SQL wich will delete a substitued product, from the database, definitely.
		"""

		self.product_id = product_id

		self.r_delete_substitued_product = (""" DELETE FROM substitued_product
												WHERE id LIKE %s """)
		self.cursor.execute(self.r_delete_substitued_product, (self.product_id,))
		self.conn.commit()


