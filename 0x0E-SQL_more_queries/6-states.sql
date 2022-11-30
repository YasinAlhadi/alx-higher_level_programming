-- create the database hbtn_0d_usa and the table states

-- creaye database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- ctreate table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
