SELECT DISTINCT buyer_id
FROM Sales join product using(product_id)
WHERE product_name = 'S8'
AND buyer_id not in (
    SELECT DISTINCT buyer_id
    FROM Sales join product using(product_id)
    WHERE product_name = 'iPhone'
    );

SELECT buyer_id
FROM Sales JOIN Product USING(product_id)
GROUP BY buyer_id
HAVING SUM(CASE WHEN product_name = 'S8' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN product_name = 'iPhone' THEN 1 ELSE 0 END) = 0;
