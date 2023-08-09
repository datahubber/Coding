SELECT 
    u.product_id, 
    ROUND(SUM(p.price * u.units) / SUM(u.units), 2) AS average_price
FROM unitssold u
JOIN prices p ON 1=1
    AND p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id;
