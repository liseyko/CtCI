select email from (select Email, count(Email) as cnt from  Person group by email) as subq where cnt>1;
select Email from Person group by Email having count(Email) > 1;