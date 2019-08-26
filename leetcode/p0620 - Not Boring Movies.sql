SELECT *
FROM cinema
WHERE MOD(id, 2) = 1 AND NOT description = 'boring'
ORDER BY rating DESC