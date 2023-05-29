SELECT MONTH(sales.OrderDate) AS mes, COUNT(*) as total_vendas
FROM sales
GROUP BY mes
ORDER BY total_vendas DESC
LIMIT 1