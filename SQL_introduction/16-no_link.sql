-- Script to list all records in second_table with a name that is not NULL and not an empty string ordered by score (highest score first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
