SELECT d.name 'Department', e1.name 'Employee', e1.salary
FROM Employee e1
  INNER JOIN Department d ON e1.DepartmentId = d.id
  LEFT JOIN Employee e2 ON e1.DepartmentId = e2.DepartmentId AND e1.salary <= e2.salary
group by e1.Id
having count(distinct e2.Salary) <= 3
order by e1.DepartmentId, e1.salary DESC