-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM Superstore;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM Superstore;

-- Sales by Category
SELECT Category,
SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Region
SELECT Region,
SUM(Profit) AS Total_Profit
FROM Superstore
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Top 10 Products
SELECT [Product Name],
SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Sales by Segment
SELECT Segment,
SUM(Sales) AS Total_Sales
FROM Superstore
GROUP BY Segment;
