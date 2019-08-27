select activity_date as day, count(distinct user_id) as active_users
from Activity
group by activity_date
HAVING activity_date between '2019-06-28' and '2019-07-27';

select activity_date as day, count(distinct user_id) as active_users 
from Activity
where datediff('2019-07-27', activity_date) <30
group by activity_date
