-- create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create a table cities in the hbtn_0d_usa database with the following columns:
-- id: integer (auto increment, primary key)
-- state_id: integer (cannot be null, foreign key referencing states.id)
-- name: string (256 characters at most, cannot be null)
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);