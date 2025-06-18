SELECT sale_date, SUM(price * quantity) AS daily_revenue
FROM retail_sales
GROUP BY sale_date
ORDER BY sale_date;

SELECT product, SUM(quantity) AS total_sold
FROM retail_sales
GROUP BY product
ORDER BY total_sold DESC
LIMIT 5;

SELECT 
    SUM(return_count) AS total_returns,
    SUM(quantity) AS total_sold,
    ROUND(SUM(return_count)::decimal / (SUM(quantity) + SUM(return_count)) * 100, 2) AS return_rate_percent
FROM retail_sales;

SELECT AVG(price) AS avg_price
FROM retail_sales;
