# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM person
LEFT JOIN Address
ON Person.personID = Address.personID;