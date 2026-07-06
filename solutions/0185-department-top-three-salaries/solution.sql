# Write your MySQL query statement below
# Write your MySQL query statement below
select d.name as department,
    e1.name as Employee,
    e1.salary as salary
from employee as e1 inner join department d
on e1.departmentid = d.id
where 3 > (
    select count(distinct (e2.salary))
    from employee as e2
    where e1.salary < e2.salary and 
    e1.departmentid = e2.departmentid
)
