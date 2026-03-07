SELECT COUNT(*)
FROM transactions;

SELECT SUM(amount)
FROM transactions;

SELECT AVG(amount)
FROM transactions;

SELECT transaction_type, COUNT(*)
FROM transactions
GROUP BY transaction_type;

SELECT transaction_type, SUM(fee_amount)
FROM transactions
GROUP BY transaction_type;

SELECT 
u.user_id,
COUNT(t.transaction_id) AS transaction_count
FROM users u
JOIN transactions t
ON u.user_id = t.user_id
GROUP BY u.user_id
ORDER BY transaction_count DESC;
