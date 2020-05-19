
SET NAMES utf8;


--
-- Table structure for table `Category`
--


CREATE TABLE IF NOT EXISTS Category (
id int unsigned NOT NULL AUTO_INCREMENT,
name varchar(200) NOT NULL,
CONSTRAINT Category_pk PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET utf8mb4;


--
-- Table structure for table `Store`
--


CREATE TABLE IF NOT EXISTS Store (
id int unsigned NOT NULL AUTO_INCREMENT,
name varchar(200) NOT NULL,
CONSTRAINT Stores_pk PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET utf8mb4;


--
-- Table structure for table `Product`
--


CREATE TABLE IF NOT EXISTS Product (
id int unsigned NOT NULL AUTO_INCREMENT,
name varchar(200) NOT NULL,
nutriscore char(1) NULL,
nutriscore_value int(1) NULL,
url text NOT NULL,
substitut_id int unsigned NULL,
category_id int unsigned NULL,
category_name varchar(200) NOT NULL,
CONSTRAINT Product_pk PRIMARY KEY (id),
CONSTRAINT Category_Product_fk
    FOREIGN KEY (category_id)
    REFERENCES Category (id)
)
ENGINE=InnoDB DEFAULT CHARSET utf8mb4;


--
-- Table structure for table `Association`
--


CREATE TABLE IF NOT EXISTS Association (
id int unsigned NOT NULL AUTO_INCREMENT,
product_id int unsigned NOT NULL,
store_id int unsigned NOT NULL,
CONSTRAINT Association_id_pk PRIMARY KEY (id),
CONSTRAINT Product_Association_fk
    FOREIGN KEY (product_id)
    REFERENCES Product (id),
CONSTRAINT Store_Association_fk
    FOREIGN KEY (store_id)
    REFERENCES Store (id)
)
ENGINE=InnoDB DEFAULT CHARSET utf8mb4;





