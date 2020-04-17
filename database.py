#!/usr/bin/python3
# -*- coding: Utf-8 -*

from classes12 import *


create_table = MySqlConnector()


create_table.cursor.execute("""
	DROP TABLE IF EXISTS category;
""")

create_table.cursor.execute("""
	DROP TABLE IF EXISTS product;
""")

create_table.cursor.execute("""
	SET NAMES utf8mb4;
""")

# Create table category.

create_table.cursor.execute("""
	CREATE TABLE Category (
	id int(10) unsigned NOT NULL AUTO_INCREMENT,
	name varchar(200) NOT NULL,
	PRIMARY KEY (id)
	)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")


# Create table product.

create_table.cursor.execute("""
	CREATE TABLE Product (
	id int(10) unsigned NOT NULL AUTO_INCREMENT,
	name varchar(200) NOT NULL,
	nutriscore char(1) NULL,
	nutriscore_value int(1) NULL,
	url text NOT NULL,
	stores text NOT NULL,
	substitut_id int(10) NOT NULL DEFAULT '0',
	category_id int(10) unsigned NULL,
	category_name varchar(100) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""")

# Create table substitued product.

create_table.cursor.execute("""
	CREATE TABLE IF NOT EXISTS SubstituedProduct (
	id int(10) unsigned NOT NULL AUTO_INCREMENT,
	name varchar(200) NOT NULL,
	nutriscore char(1) NULL,
	nutriscore_value int(1) NULL,
	url text NOT NULL,
	stores text NOT NULL,
	category_id int(10) unsigned NULL,
	category_name varchar(100) NULL,
	PRIMARY KEY (id)
)
ENGINE=InnoDB;
""")

create_table.conn.commit()




