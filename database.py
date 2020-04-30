#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Program database.
"""

from classes_mysql import (MySqlConnector)


class Database():
    """
    This class allows us to create tables:
    category, product, store, association and substitued_product in mysql.
    """

    def __init__(self):

        self.mysql = MySqlConnector()
        self.mysql.connection()

    def table(self):
        """
        This method allows us to create tables.
        """

        self.mysql.cursor.execute("""
            SET NAMES utf8;
        """)

        # Create category table.

        self.mysql.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Category (
            id int unsigned NOT NULL AUTO_INCREMENT,
            name varchar(200) NOT NULL,
            CONSTRAINT Category_pk PRIMARY KEY (id)
            )
        ENGINE=InnoDB;
        """)

        # Create store table.

        self.mysql.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Store (
            id int unsigned NOT NULL AUTO_INCREMENT,
            name varchar(200) NOT NULL,
            CONSTRAINT Stores_pk PRIMARY KEY (id)
            )
        ENGINE=InnoDB DEFAULT CHARSET utf8mb4;
        """)

        # Create product table.

        self.mysql.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Product (
            id int unsigned NOT NULL AUTO_INCREMENT,
            name varchar(200) NOT NULL,
            nutriscore char(1) NULL,
            nutriscore_value int(1) NULL,
            url text NOT NULL,
            substitut_id int unsigned NULL,
            category_id int unsigned NULL,
            category_name varchar(200) NOT NULL,
            CONSTRAINT Product_pk PRIMARY KEY (id)
        )
        ENGINE=InnoDB DEFAULT CHARSET utf8mb4;
        """)

        # Create association table.

        self.mysql.cursor.execute("""
          CREATE TABLE IF NOT EXISTS Association (
          id int unsigned NOT NULL AUTO_INCREMENT,
          product_id int unsigned NOT NULL,
          store_id int unsigned NOT NULL,
          CONSTRAINT Association_id_pk PRIMARY KEY (id)
          )
        ENGINE=InnoDB DEFAULT CHARSET utf8mb4;
        """)

        # Create substitued product table.

        self.mysql.cursor.execute("""
            CREATE TABLE IF NOT EXISTS SubstituedProduct (
            id int unsigned NOT NULL AUTO_INCREMENT,
            name varchar(200) NOT NULL,
            nutriscore char(1) NULL,
            nutriscore_value int(1) NULL,
            url text NOT NULL,
            store text NOT NULL,
            category_id int(10) unsigned NULL,
            category_name varchar(200) NOT NULL, 
            CONSTRAINT SubstituedProduct_pk PRIMARY KEY (id)
        )
        ENGINE=InnoDB DEFAULT CHARSET utf8mb4;
        """)

        self.mysql.conn.commit()

    def foreign_key(self):
        """
        This method allows us to create foreign keys into tables mysql.
        """

        # Create foreign key in 'Product' table.

        self.mysql.cursor.execute("""
            ALTER TABLE Product ADD CONSTRAINT SubstituedProduct_Product_fk
            FOREIGN KEY (substitut_id)
            REFERENCES SubstituedProduct (id)
            ON DELETE SET NULL;
        """)

        self.mysql.cursor.execute("""
            ALTER TABLE Product ADD CONSTRAINT Category_Product_fk
            FOREIGN KEY (category_id)
            REFERENCES Category (id);
        """)

        # Create foreign key in 'Association' table.

        self.mysql.cursor.execute("""
            ALTER TABLE Association ADD CONSTRAINT Product_Association_fk
            FOREIGN KEY (product_id)
            REFERENCES Product (id);
        """)

        self.mysql.cursor.execute("""
            ALTER TABLE Association ADD CONSTRAINT Store_Association_fk
            FOREIGN KEY (store_id)
            REFERENCES Store (id);
        """)

        self.mysql.conn.commit()
