SELECT territories.*, COUNT(sales.TerritoryKey) AS Vendas_por_Territorio
FROM territories
JOIN sales ON territories.SalesTerritoryKey = sales.TerritoryKey
GROUP BY territories.SalesTerritoryKey
ORDER BY Vendas_por_Territorio DESC
LIMIT 1;