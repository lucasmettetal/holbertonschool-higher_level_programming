-- create a table id_not_null with the following columns:
-- id: integer (cannot be null, default value is 1)
-- name: string (256 characters at most)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);