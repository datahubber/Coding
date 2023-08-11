SELECT employee_id
FROM Employees e
WHERE
    salary < 30000 AND manager_id NOT IN (select employee_id from employees as c)
order by employee_id

select
  case
    when seat.id % 2 <> 0 and seat.id = (select count(*) from seat) then seat.id
    when seat.id % 2 = 0 then seat.id - 1
    else
      seat.id + 1
    end as id,
    student
from seat
order by id

(Select u.name as results 
from MovieRating as m, Users as u 
where u.user_id = m.user_id Group By m.user_id 
Order by count(m.user_id) desc, u.name limit 1)
union all
(Select m.title as results
from MovieRating as r, Movies as m
where m.movie_id = r.movie_id 
and r.created_at like "2020-02-%"
Group By r.movie_id 
Order by avg(r.rating) desc, m.title limit 1);


select
    visited_on,
    (
        select sum(amount)
        from customer
        where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on)
        as amount,
    round(
        (select sum(amount) / 7
        from customer
        where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on), 2)
    as average_amount
from customer c
where visited_on >= (
    select date_add(min(visited_on), interval 6 day)
    from customer
)
group by visited_on;

with base as(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted)
select id, count(*) num  from base group by 1 order by 2 desc limit 1

select d.name Department, e1.name employee, e1.salary
from employee e1
join department d
on e1.departmentId = d.id
where 3 > (select count(distinct(e2.salary))
            from employee e2
            where e2.salary > e1.salary
            and e1.departmentId = e2.departmentId)
