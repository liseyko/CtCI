# Write your MySQL query statement below
UPDATE salary SET sex = IF(sex='f','m','f');
update salary set sex=char(11^ascii(sex));
UPDATE salary SET sex = CASE 
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;