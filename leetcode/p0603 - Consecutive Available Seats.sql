select seat_id
from cinema
where (seat_id-1 in 
        (select seat_id
         from cinema
         where free  = 1) 
      or seat_id+1 in 
        (select seat_id
        from cinema
        where free  = 1)
      ) and free = 1

select distinct c1.seat_id
from cinema c1 join cinema c2 
  on abs(c1.seat_id - c2.seat_id) = 1 
  and c1.free = 1 and c2.free = 1
order by c1.seat_id
