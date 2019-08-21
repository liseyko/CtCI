SELECT DISTINCT product_id, product_name
FROM Product join Sales using (product_id)
WHERE sale_date between '2019-01-01' and '2019-03-31'
AND product_id not in (
    select distinct product_id from Sales
    where sale_date not between '2019-01-01' and '2019-03-31'
    )

SELECT product_id, product_name
FROM Sales
JOIN Product
Using(product_id)
GROUP BY product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'
