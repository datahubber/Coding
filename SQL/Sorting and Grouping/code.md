SELECT teacher_id, count(distinct subject_id) as cnt
FROM Teacher
GROUP BY teacher_id;

SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN 
(SELECT product_id, MIN(year) as year
From Sales
group by product_id);

SELECT class
FROM (select class, count(distinct student) as num from Courses 
group by class) as temp
WHERE num >=5;

SELECT 
  user_id,
  count(follower_id) as followers_count
FROM Followers
group by user_id
order by user_id;

SELECT max(num) as num
FROM (select num from mynumbers group by num having count(num) = 1)
AS C

SELECT customer_id FROM Customer group by customer_id
HAVING COUNT(DISTINCT product_key) = (select count(distinct product_key) from product)
