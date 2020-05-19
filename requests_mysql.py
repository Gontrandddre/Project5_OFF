#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program class, requests SQL.
"""

import mysql.connector
from mysql.connector import errorcode


class MySqlConnector():
    """
    This class allows us to connect on mysql first, and communcate with database.
    """

    def __init__(self):

        self.cursor = ''
        self.rows = ''

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

    def request_add_data(self, request, data):
        """
        this method allows us to insert data in mysql database.
        """

        self.cursor.execute(request, data)
        self.conn.commit()

    def request_searchall_data(self, request, **data):
        """
        this method allows us to return all data from a SQL request.
        """

        self.cursor.execute(request, **data)
        self.rows = self.cursor.fetchall()
        self.conn.commit()
        return self.rows

    def request_searchmany_data(self, request, data, many):
        """
        This method allows us to return a quite of few data from a SQL request.
        """

        self.cursor.execute(request, data)
        self.rows = self.cursor.fetchmany(many)
        self.conn.commit()
        return self.rows

    def request_update_data(self, request, data):
        """
        This method allow us to update data in mysql database.
        """

        self.cursor.execute(request, data)
        self.conn.commit()
