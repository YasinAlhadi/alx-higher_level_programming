-- creates the database hbtn_0d_2 and the user user_0d_2
-- user user_0d_2 with SELECT privilege in the database hbtn_0d_2

-- create database
CREATE DATABASE IF NOt EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant previlage
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
