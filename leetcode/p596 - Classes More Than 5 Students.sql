# Write your MySQL query statement below
select class from (
    select count(DISTINCT student) as n, class 
    from courses 
    group by class
    ) as c
where n >= 5
