SELECT employee_id
FROM Employees e
WHERE
    salary < 30000 AND manager_id NOT IN (select employee_id from employees as c)
order by employee_id
