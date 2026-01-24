--Task 1.1
SELECT c.Name, o.Product, o.Amount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;

-- Task 1.2: Display all customers even if they have not placed any orders
SELECT c.Name, o.Product, o.Amount
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID;

-- Task 1.3: Display only orders with amount greater than 20,000
SELECT c.Name, o.Product, o.Amount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.Amount > 20000;

-- Task 2.4: Find the total purchase amount for each customer
SELECT c.Name, SUM(o.Amount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.Name;

-- Task 2.5: Display customer names whose total spending is greater than 40,000
SELECT c.Name, SUM(o.Amount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.Name
HAVING SUM(o.Amount) > 40000;

-- Task 2.6: Find the average order amount for each city
SELECT c.City, AVG(o.Amount) AS AvgOrderAmount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.City;

-- Task 3.7: Display cities where total sales exceed 50,000
SELECT c.City, SUM(o.Amount) AS TotalSales
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.City
HAVING SUM(o.Amount) > 50000;

-- Task 3.8: Show customers who have placed more than one order
SELECT c.Name, COUNT(o.OrderID) AS OrderCount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.Name
HAVING COUNT(o.OrderID) > 1;

-- Task 4.9: Find customers who have spent more than the average order amount
SELECT c.Name, SUM(o.Amount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.Name
HAVING SUM(o.Amount) > (
    SELECT AVG(Amount)
    FROM Orders
);

-- Task 4.10: Display the name of the customer who placed the highest value order
SELECT c.Name, o.Amount
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.Amount = (
    SELECT MAX(Amount)
    FROM Orders
);

-- Task 4.11: Find customers who have never placed an order
SELECT Name
FROM Customers
WHERE CustomerID NOT IN (
    SELECT CustomerID
    FROM Orders
);