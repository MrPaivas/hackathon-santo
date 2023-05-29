SELECT customers.*, COUNT(sales.CustomerKey) AS compras
FROM customers
JOIN sales ON customers.CustomerKey = sales.CustomerKey
GROUP BY customers.CustomerKey
ORDER BY compras DESC
LIMIT 1;
 