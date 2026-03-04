-- list all records in second_table with a score higher than or equal to 10 ordered by score (highest score first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
