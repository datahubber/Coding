select
    user_id,
    concat(UPPER(SUBSTR(name,1,1)), LOWER(substr(name,2))) AS name
from users
order by user_id

select patient_id, patient_name, conditions
from patients
where conditions REGEXP '\\bDIAB1'

delete p1
from person p1, person p2
where p1.email = p2.email and p1.id > p2.id

select 
    max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee)

select
    sell_date,
    count(distinct product) as num_sold,
    group_concat(distinct product order by product asc separator ',') as products
from activities
group by sell_date
order by sell_date

select
    p.product_name as product_name,
    sum(o.unit) as unit
from products p
left join orders o on p.product_id = o.product_id
where year(o.order_date) = '2020' and month(o.order_date) = '02'
group by p.product_id
having sum(o.unit) >=100

select *
from users
where regexp_like(mail, '^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode.com')

SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$';
