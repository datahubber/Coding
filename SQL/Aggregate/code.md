SELECT 
    u.product_id, 
    ROUND(SUM(p.price * u.units) / SUM(u.units), 2) AS average_price
FROM unitssold u
JOIN prices p ON 1=1
    AND p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id;

SELECT
    project_id,
    ROUND(SUM(e.experience_years) / COUNT(e.experience_years),2) AS average_years
FROM Project p
JOIN Employee e ON
    p.employee_id = e.employee_id
GROUP BY project_id

SELECT
    contest_id,
    ROUND(COUNT(DISTINCT user_id)*100 / (select COUNT(user_id) from Users),2) AS percentage
FROM Register r
GROUP BY contest_id
ORDER BY percentage DESC, contest_id

SELECT round(sum(customer_pref_delivery_date=order_date) * 100 / count(order_date), 2) as immediate_percentage
FROM Delivery 
WHERE (customer_id, order_date) IN (select customer_id, min(order_date) as first_order
FROM Delivery
group by customer_id)

**
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id)
