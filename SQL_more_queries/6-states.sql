-- create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table states in the hbtn_0d_usa database with the following columns:
-- id: integer (auto increment, primary key)
-- name: string (256 characters at most, cannot be null)
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);