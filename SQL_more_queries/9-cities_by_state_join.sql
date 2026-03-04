-- Write a SQL query to list all the cities of California in the database hbtn_0d_usa. The states table contains the state name and state id. The cities table contains the city name and state id. Your query should use a JOIN.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;