-- lists all cities contained in the database hbtn_0d_usa
-- Results ordered by cities.id
SELECT id , name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id;