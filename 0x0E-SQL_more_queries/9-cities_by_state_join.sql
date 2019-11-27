-- Lists all the cities in the database hbtn_0d_usa 
SELECT cities.id, cities.name, state.name
FROM cities 
INNER JOIN states 
ON cities.states_id = states.id
ORDER BY cities.id;