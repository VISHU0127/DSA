# Write your MySQL query statement below
select 
    CASE
        WHEN
            id = (select MAX(id) from seat) and MOD(id, 2) = 1
            then id
        WHEN 
            MOD(id, 2) = 1
            then id + 1
        else
            id - 1
    end as id, student
from Seat
order by id
