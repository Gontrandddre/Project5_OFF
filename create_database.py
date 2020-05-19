#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program class, generate structure database:
- Table 'Category';
- Table 'Store';
- Table 'Product';
- Table 'Association'.
"""

from requests_mysql import (MySqlConnector)


class Table():
    """
    This class allow us to generate structure database with a 'filename.sql'.
    """

    def __init__(self):

        self.mysql = MySqlConnector()
        self.mysql.connection()

    def generate_structure_database(self, filename):
        """
        This method allow us to generate tables structure for database.
        """

        file = open(filename, 'r')
        sql = " ".join(file.readlines())
        self.mysql.cursor.execute(sql)
