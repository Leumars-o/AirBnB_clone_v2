-- Script creates a MYSQL server with:
--  a database called hbnb_dev_db
--  a user called hbnb_dev with the password hbnb_dev_pwd
--  all privileges on the database to the user

-- creates a database if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create the user if it doesnt exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;
