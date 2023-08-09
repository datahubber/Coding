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
