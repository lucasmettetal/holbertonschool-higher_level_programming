-- create a table unique_id with the following columns:
-- id: integer (default value is 1, must be unique)
-- name: string (256 characters at most)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);