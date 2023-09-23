-- Drop Sales Fact Table
DROP TABLE IF EXISTS SalesFact;

-- Drop Product Dimension Table
DROP TABLE IF EXISTS ProductDimension;

-- Drop Vendor Dimension Table
DROP TABLE IF EXISTS VendorDimension;

-- Drop Subcategory Dimension Table
DROP TABLE IF EXISTS SubcategoryDimension;

-- Drop Category Dimension Table
DROP TABLE IF EXISTS CategoryDimension;

-- Drop Date Dimension Table
DROP TABLE IF EXISTS DateDimension;

-- Drop SalesTerritoryDimension Table
DROP TABLE IF EXISTS SalesTerritoryDimension;

-- Drop StateDimension Table
DROP TABLE IF EXISTS StateDimension;

-- Drop CountryDimension Table
DROP TABLE IF EXISTS CountryDimension;

-- Date Dimension Table
CREATE TABLE DateDimension (
    date_id INT PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    day INT,
    day_name VARCHAR(20),
    month_name VARCHAR(20),
    full_date VARCHAR(50)
);

CREATE INDEX IDX_DateDimension_Year ON DateDimension (year);
CREATE INDEX IDX_DateDimension_Month ON DateDimension (month);
CREATE INDEX IDX_DateDimension_Day ON DateDimension (day);
CREATE INDEX IDX_DateDimension_MonthName ON DateDimension (month_name);

-- Category Dimension Table
CREATE TABLE CategoryDimension (
    category_id INT PRIMARY KEY,
    category_name NVARCHAR(255)
);

CREATE INDEX IDX_CategoryDimension_CategoryName ON CategoryDimension (category_name);

-- Subcategory Dimension Table
CREATE TABLE SubcategoryDimension (
    subcategory_id INT PRIMARY KEY,
    subcategory_name NVARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES CategoryDimension(category_id)
);

CREATE INDEX IDX_SubcategoryDimension_SubcategoryName ON SubcategoryDimension (subcategory_name);

-- Product Dimension Table
CREATE TABLE ProductDimension (
    product_id INT PRIMARY KEY,
    product_name NVARCHAR(255),
    subcategory_id INT,
    FOREIGN KEY (subcategory_id) REFERENCES SubcategoryDimension(subcategory_id)
);

CREATE INDEX IDX_ProductDimension_ProductName ON ProductDimension (product_name);

-- Vendor Dimension Table
CREATE TABLE VendorDimension (
    vendor_id INT PRIMARY KEY,
    vendor_name NVARCHAR(255)
);

CREATE INDEX IDX_VendorDimension_VendorName ON VendorDimension (vendor_name);

CREATE TABLE CountryDimension (
    country_id NVARCHAR(5) PRIMARY KEY,
    country_name NVARCHAR(255)
);

CREATE INDEX IDX_CountryDimension_country_name ON CountryDimension (country_name);

CREATE TABLE StateDimension (
    state_id NVARCHAR(5) PRIMARY KEY,
    country_id NVARCHAR(5),
    state_name NVARCHAR(255),

	FOREIGN KEY (country_id) REFERENCES CountryDimension(country_id),
);

CREATE INDEX IDX_country_id ON StateDimension (country_id);
CREATE INDEX IDX_state_name ON StateDimension (state_name);

-- Sales Territory Dimension Table
CREATE TABLE SalesTerritoryDimension (
    territory_id INT PRIMARY KEY,
    country_id NVARCHAR(5),
	
	FOREIGN KEY (country_id) REFERENCES CountryDimension(country_id),
);

CREATE INDEX IDX_SalesTerritoryDimension_state_country_id ON SalesTerritoryDimension (country_id);

-- Sales Fact Table
CREATE TABLE SalesFact (
    sales_id INT IDENTITY(1, 1) PRIMARY KEY,
    date_id INT,
    product_id INT,
    vendor_id INT,
	territory_id INT,
    quantity_sold INT,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (date_id) REFERENCES DateDimension(date_id),
    FOREIGN KEY (product_id) REFERENCES ProductDimension(product_id),
    FOREIGN KEY (vendor_id) REFERENCES VendorDimension(vendor_id),
	FOREIGN KEY (territory_id) REFERENCES SalesTerritoryDimension(territory_id)
);

CREATE INDEX IDX_SalesFact_DateId ON SalesFact (date_id);
CREATE INDEX IDX_SalesFact_ProductId ON SalesFact (product_id);
CREATE INDEX IDX_SalesFact_VendorId ON SalesFact (vendor_id);
CREATE INDEX IDX_SalesFact_QuantitySold ON SalesFact (quantity_sold);
CREATE INDEX IDX_SalesFact_TotalAmount ON SalesFact (total_amount);