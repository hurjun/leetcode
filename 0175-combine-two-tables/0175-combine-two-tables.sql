# Write your MySQL query statement below
Select 
    p.firstName, p.lastname, a.city, a.state from Person p Left Join Address a on p.personId=a.personId