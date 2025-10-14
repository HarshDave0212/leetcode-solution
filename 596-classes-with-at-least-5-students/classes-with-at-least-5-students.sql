# Write your MySQL query statement below
SELECT class 
from Courses 
GROUP BY class 
having count(class)>4