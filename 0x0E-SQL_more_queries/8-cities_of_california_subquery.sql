-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- Lists all cities
SEELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE 'name' = "California") ORDER BY id ASC;
