# Write your MySQL query statement below
SELECT 
    d.Name as Department,
    e.Name as Employee,
    Salary
FROM Employee e JOIN Department d ON e.DepartmentId = d.Id
WHERE (d.id, e.Salary) IN (
    SELECT DepartmentId, max(salary) 
    FROM Employee
    GROUP BY DepartmentId
    )

