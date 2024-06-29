With Tbl_Ventas as (
SELECT 
    YEAR(sod.OrderDate) AS Anho,
	Month(sod.OrderDate) AS Mes,
    p.Name AS Nombre_Producto,
    SUM(sd.LineTotal) AS TotalVentas,
    COUNT(p.Name) AS CantidadProductos,
    ROW_NUMBER() OVER (PARTITION BY YEAR(sod.OrderDate) ORDER BY SUM(sd.LineTotal) DESC) AS Ranking,
	SUM(SUM(sd.LineTotal)) OVER (PARTITION BY YEAR(sod.OrderDate)) AS TotalMontoAhno,
	sum(count(p.Name)) OVER (PARTITION BY YEAR(sod.OrderDate)) AS TotalCantidadAhno
FROM 
    AdventureWorks2017.Sales.SalesOrderDetail AS sd 
INNER JOIN 
    AdventureWorks2017.Production.Product AS p ON sd.ProductID = p.ProductID
INNER JOIN 
    AdventureWorks2017.Sales.SalesOrderHeader AS sod ON sod.SalesOrderID = sd.SalesOrderID
GROUP BY 
    YEAR(sod.OrderDate),
	Month(sod.OrderDate),
    p.Name
)
Select Anho,
	Mes,
	Nombre_Producto,
	TotalVentas,
	CantidadProductos,
	Ranking,
	(TotalVentas/TotalMontoAhno) as ParticipacionAnual,
	TotalCantidadAhno
From Tbl_Ventas
ORDER BY 
    Anho,
    Nombre_Producto