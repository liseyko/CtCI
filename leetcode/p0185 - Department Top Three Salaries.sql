SELECT d.name 'Department', e1.name 'Employee', e1.salary
FROM Employee e1
  INNER JOIN Department d ON e1.DepartmentId = d.id
  LEFT JOIN Employee e2 ON e1.DepartmentId = e2.DepartmentId AND e1.salary <= e2.salary
group by e1.Id
having count(distinct e2.Salary) <= 3
order by e1.DepartmentId, e1.salary DESC;

select d.Name Department, e1.Name Employee, e1.Salary
from Employee e1 
join Department d
on e1.DepartmentId = d.Id
where 3 > (select count(distinct(e2.Salary)) 
                  from Employee e2 
                  where e2.Salary > e1.Salary 
                  and e1.DepartmentId = e2.DepartmentId
                  );
