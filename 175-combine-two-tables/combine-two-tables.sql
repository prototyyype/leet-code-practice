# Write your MySQL query statement below
-- Report firstName, lastName, city, state
-- if address not present, report Null

SELECT p.firstName,
p.lastName,
a.city,
a.state
FROM Person p 
LEFT JOIN Address a on p.personID = a.personID;