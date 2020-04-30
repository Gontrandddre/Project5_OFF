#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program class, requests SQL.
"""

import mysql.connector
from mysql.connector import errorcode


class MySqlConnector():
    """
    This class allows us to connect on mysql first, and to create request SQL.
    """

    def __init__(self):

        self.p_id = ''
        self.c_id = ''

        self.data_p = ''
        self.data_c = ''
        self.data_s = ''
        self.data_a = ''

        self.r_add_category = ''
        self.r_add_product = ''
        self.r_add_store = ''
        self.r_add_association = ''

        self.r_search_category = ''
        self.r_search_product = ''
        self.r_search_substitute_product = ''
        self.r_search_substitued_product = ''
        self.r_search_store = ''
        self.r_search_product_stores = ''

        self.r_save_substitute_product = ''
        self.r_delete_substitued_product = ''
        self.r_add_substitut_id = ''

        self.rows1 = ''
        self.rows2 = ''
        self.rows3 = ''
        self.rows4 = ''
        self.rows5 = ''
        self.rows6 = ''

        self.cursor = ''

        self.connection()

    def connection(self):
        """
        This method allows us to connect to our database MySQL.
        """

        try:
            self.conn = mysql.connector.connect(host='localhost',
                                                user='user_p5',
                                                password='iutgea',
                                                database='p5')

        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')

            else:
                print(err)

        else:
            self.cursor = self.conn.cursor(buffered=True)

    def request_add_product(self, data_p):
        """
        This method allows us to create a request SQL,
        wich will insert the data product from OpenFoodFact into our table 'Product'.
        """

        self.data_p = data_p

        self.r_add_product = (""" INSERT INTO Product (name,
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

        self.cursor.execute(self.r_add_product, self.data_p)
        self.conn.commit()

    def request_add_category(self, data_c):
        """
        This method allows to create a request SQL,
        wich will insert the data category into our table 'Category'.
        """

        self.data_c = data_c

        self.r_add_category = (""" INSERT INTO Category (name)
                                   VALUES (%s)
                               """)

        self.cursor.execute(self.r_add_category, self.data_c)
        self.conn.commit()

    def request_add_store(self, data_s):
        """
        This method allows to create a request SQL,
        wich will insert the data category into our table 'Category'.
        """

        self.data_s = data_s

        self.r_add_store = (""" INSERT INTO Store (name)
                                VALUES (%s)
                            """)

        self.cursor.execute(self.r_add_store, self.data_s)
        self.conn.commit()

    def request_add_association(self, data_a):
        """
        This method allows to create a request SQL,
        wich will insert the data association into our table 'Association'.
        """

        self.data_a = data_a

        self.r_add_association = (""" INSERT INTO Association (product_id,
                                                               store_id)
                                      VALUES (%s,
                                              %s)
                                  """)

        self.cursor.execute(self.r_add_association, self.data_a)
        self.conn.commit()

    def request_search_category(self):
        """
        This method allows us to create a request SQL,
        wich will search data category in our table 'Category'.
        """

        self.r_search_category = (""" SELECT id,
                                             name
                                      FROM Category
                                  """)

        self.cursor.execute(self.r_search_category)
        self.rows1 = self.cursor.fetchall()
        self.conn.commit()

    def request_search_store(self):
        """
        This method allows us to create a request SQL,
        wich will search data store in our table 'Store'.
        """

        self.r_search_store = (""" SELECT id,
                                          name
                                   FROM Store
                               """)

        self.cursor.execute(self.r_search_store)
        self.rows2 = self.cursor.fetchall()
        self.conn.commit()

    def request_search_product(self, c_id):
        """
        This method allows us to create a request SQL,
        wich will search data product in our table 'Product'.
        """

        self.c_id = c_id

        self.r_search_product = (""" SELECT id,
                                            name,
                                            nutriscore
                                     FROM Product
                                     WHERE category_id LIKE %s
                                     ORDER BY RAND()
                                     LIMIT 15
                                 """)

        self.cursor.execute(self.r_search_product, (self.c_id,))
        self.rows3 = self.cursor.fetchmany(15)
        self.conn.commit()

    def request_search_substitute_product(self, c_id):
        """
        This method allows us to create a request SQL,
        wich will search substitute product in our table 'Product'.
        For that, we collect the best of 5 nutriscore in the same category.
        """

        self.c_id = c_id

        self.r_search_substitute_product = (""" SELECT p.id,
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

        self.cursor.execute(self.r_search_substitute_product, (self.c_id,))
        self.rows4 = self.cursor.fetchmany(5)
        self.conn.commit()

    def request_search_substitued_product(self):
        """
        This method allows us to create a request SQL,
        wich will search data from the 'SubstituedProduct' table (user database).
        """

        self.r_search_substitued_product = (""" SELECT DISTINCT id,
                                                                name,
                                                                nutriscore,
                                                                category_name,
                                                                url,
                                                                store
                                                FROM SubstituedProduct
                                            """)

        self.cursor.execute(self.r_search_substitued_product)
        self.conn.commit()
        self.rows5 = self.cursor.fetchall()

    def request_search_product_stores(self):
        """
        This method allows us to create a request SQL,
        wich will search data store in our table 'Store'.
        """

        self.r_search_product_stores = (""" SELECT MAX(id)
                                            FROM Product
                                        """)

        self.cursor.execute(self.r_search_product_stores)
        self.conn.commit()
        self.rows6 = self.cursor.fetchall()

    def request_save_substitute_product(self, p_id):
        """
        This method allows us to create a request SQL,
        to insert on our table 'SubstituedProduct',
        data from the substitute product selected by the user.
        """

        self.p_id = p_id

        self.r_save_substitute_product = (""" INSERT INTO SubstituedProduct(name,
                                                                            nutriscore,
                                                                            nutriscore_value,
                                                                            url,
                                                                            category_name,
                                                                            category_id,
                                                                            store)
                                              SELECT p.name,
                                                     p.nutriscore,
                                                     p.nutriscore_value,
                                                     p.url,
                                                     p.category_name,
                                                     p.category_id,
                                                     GROUP_CONCAT(s.name SEPARATOR ', ') as concat_name
                                              FROM Product as p
                                              JOIN association as a
                                              ON p.id = a.product_id
                                              JOIN store as s
                                              ON s.id = a.store_id
                                              WHERE p.id LIKE %s
                                              GROUP BY p.id
                                          """)

        self.cursor.execute(self.r_save_substitute_product, (self.p_id,))
        self.conn.commit()

    def request_add_substitut_id(self, p_id):
        """
        This method allows us to add substitut_id in 'Product' table,
        from 'SubstituedProduct' table when we save an substitute product.
        """

        self.p_id = p_id

        self.r_add_substitut_id = (""" UPDATE Product
                                       SET substitut_id = (SELECT MAX(id)
                                                           FROM SubstituedProduct)
                                       WHERE id LIKE %s
                                   """)
        self.cursor.execute(self.r_add_substitut_id, (self.p_id,))
        self.conn.commit()

    def request_delete_substitued_product(self, p_id):
        """
        This method allows us to create a request SQL,
        wich will delete a substitued product, from the user database, definitely.
        """

        self.p_id = p_id

        self.r_delete_substitued_product = (""" DELETE FROM SubstituedProduct
                                                WHERE id LIKE %s
                                            """)

        self.cursor.execute(self.r_delete_substitued_product, (self.p_id,))
        self.conn.commit()
