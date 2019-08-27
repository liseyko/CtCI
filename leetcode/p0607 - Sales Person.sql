select name 
from salesperson
where name not in (
    select s.name
    from salesperson s join orders o join company c 
     ON o.com_id = c.com_id and o.sales_id = s.sales_id
    WHERE c.name = 'RED'
    );

select s.name 
from salesperson s
where s.sales_id not in (
    select o.sales_id
    from orders o join company c 
     ON o.com_id = c.com_id
    WHERE c.name = 'RED'
    )