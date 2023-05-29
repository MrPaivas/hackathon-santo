SELECT subcategories.ProductSubcategoryKey, products.ProductKey, sales.*, COUNT(*) AS total_repeticoes
FROM sales
JOIN products ON sales.ProductKey = products.ProductKey
JOIN subcategories ON products.ProductSubcategoryKey = subcategories.ProductSubcategoryKey
JOIN categories ON subcategories.ProductCategoryKey = categories.ProductCategoryKey
WHERE categories.ProductCategoryKey = 1
GROUP BY sales.ProductKey
ORDER BY total_repeticoes DESC
LIMIT 10;
