-- creates the database hbtn_0d_usa and the table cities
-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use databse
USE hbtn_0d_usa;
-- Create a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCE states(id));
