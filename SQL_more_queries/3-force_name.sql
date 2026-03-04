-- create a table force_name with the following columns:
-- id: integer
-- name: string (256 characters at most, cannot be null)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);