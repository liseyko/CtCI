SELECT name, bonus
FROM Employee LEFT JOIN Bonus USING(empId)
WHERE bonus < 1000 or bonus is null
