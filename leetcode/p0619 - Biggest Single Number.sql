SELECT 
(
SELECT *
FROM my_numbers
GROUP BY 1
HAVING count(*) = 1
ORDER BY num DESC
LIMIT 1
) num


select max(num) as num
from (
	select num
	from my_numbers
	group by num
	having count(*) = 1
) t