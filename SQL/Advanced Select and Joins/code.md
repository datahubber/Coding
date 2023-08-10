SELECT
    c.employee_id,
    c.name,
    COUNT(e.employee_id) as reports_count,
    round(avg(e.age)) as average_age
FROM
    Employees e
JOIN
    employees c ON
    e.reports_to = c.employee_id
group by
    employee_id
order by
    employee_id

SELECT x, y, z, 
    IF ((x+y)>z and (y+z)>x and (x+z)>y, "Yes", "No")as triangle
FROM Triangle  

SELECT employee_id
FROM Employees e
WHERE
    salary < 30000 AND manager_id NOT IN (select employee_id from employees as c)
order by employee_id

select
    employee_id,
    department_id
from employee
where primary_flag = "Y"
union
select
    employee_id,
    department_id
from employee
group by employee_id
having count(employee_id) = 1

select distinct num as ConsecutiveNums
from logs
where (id+1, num) in (select * from logs) and (id+2, num) in (select * from logs)

select distinct product_id, 10 as price
from products where product_id not in (select distinct product_id from products where change_date <='2019-08-16')
union
select product_id, new_price as price
from products where (product_id, change_date) in (select product_id, max(change_date) as date from products where change_date <='2019-08-16' group by product_id)

select person_name
from (select person_name, weight, turn, sum(weight) over(order by turn) as cum_sum from queue) x
where cum_sum <= 1000
order by turn desc limit 1;

select 
    "Low Salary" as category,
    sum(case when income < 20000 then 1 else 0 end) as accounts_count
from accounts
union
select 
    "Average Salary" category,
    sum(case when income >= 20000 and income <= 50000 then 1 else 0 end) as accounts_count
from accounts
union
select 
    "High Salary" category,
    sum(case when income > 50000 then 1 else 0 end) as accounts_count
from accounts
