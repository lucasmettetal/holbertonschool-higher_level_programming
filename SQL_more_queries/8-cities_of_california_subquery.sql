-- Write a SQL query to list all the cities of California in the database hbtn_0d_usa. The states table contains the state name and state id. The cities table contains the city name and state id. Your query should use a subquery.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;