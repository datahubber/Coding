SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;

SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
LEFT JOIN Product
ON Sales.product_id = Product.product_id;

SELECT Customer_id, count(*) AS count_no_trans FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY Customer_id;

SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature AND TO_DAYS(w1.recordDate)-TO_DAYS(w2.recordDate) = 1;

SELECT m.name 
FROM Employee e
INNER JOIN Employee m
ON e.managerId = m.id
GROUP BY e.managerId
having count(e.id) >4;  

SELECT
    s.user_id,
    round(avg(if(c.action = "confirmed",1,0)), 2) as confirmation_rate
FROM
    signups s
left join
    confirmations c on s.user_id = c.user_id
group by user_id
