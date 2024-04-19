-- Script creates a MYSQL server with:
--  a database called hbnb_dev_db
--  a user called hbnb_dev with the password hbnb_dev_pwd
--  all privileges on the database to the user

-- creates a database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the user if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
