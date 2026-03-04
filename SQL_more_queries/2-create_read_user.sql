-- create a new database hbtn_0d_2 and a new user user_0d_2 with password user_0d_2_pwd
-- give user_0d_2 only SELECT privileges on the hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';