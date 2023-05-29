-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28-Maio-2023 às 03:28
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `adventureworks`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `calendar`
--

CREATE TABLE `calendar` (
  `Date` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `categories`
--

CREATE TABLE `categories` (
  `ProductCategoryKey` int(11) NOT NULL,
  `CategoryName` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `customers`
--

CREATE TABLE `customers` (
  `CustomerKey` int(11) NOT NULL,
  `Prefix` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `BirthDate` varchar(45) NOT NULL,
  `MaritalStatus` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `EmailAddress` varchar(45) NOT NULL,
  `AnnualIncome` varchar(45) NOT NULL,
  `TotalChildren` varchar(45) NOT NULL,
  `EducationLevel` varchar(45) NOT NULL,
  `Occupation` varchar(45) NOT NULL,
  `HomeOwner` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `products`
--

CREATE TABLE `products` (
  `ProductKey` int(5) NOT NULL,
  `ProductSubcategoryKey` int(5) DEFAULT NULL,
  `ProductSKU` varchar(45) DEFAULT NULL,
  `ProductName` varchar(200) DEFAULT NULL,
  `ModelName` varchar(200) DEFAULT NULL,
  `ProductDescription` varchar(200) DEFAULT NULL,
  `ProductColor` varchar(45) DEFAULT NULL,
  `ProductSize` varchar(45) DEFAULT NULL,
  `ProductStyle` varchar(45) DEFAULT NULL,
  `ProductCost` decimal(10,2) DEFAULT NULL,
  `ProductPrice` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sales`
--

CREATE TABLE `sales` (
  `SaleKey` int(11) NOT NULL,
  `OrderDate` varchar(45) DEFAULT NULL,
  `StockDate` varchar(45) DEFAULT NULL,
  `OrderNumber` varchar(45) DEFAULT NULL,
  `ProductKey` int(5) DEFAULT NULL,
  `CustomerKey` int(5) DEFAULT NULL,
  `TerritoryKey` int(5) DEFAULT NULL,
  `OrderLineItem` int(5) DEFAULT NULL,
  `OrderQuantity` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `subcategories`
--

CREATE TABLE `subcategories` (
  `ProductSubcategoryKey` int(5) NOT NULL,
  `SubcategoryName` varchar(45) DEFAULT NULL,
  `ProductCategoryKey` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `territories`
--

CREATE TABLE `territories` (
  `SalesTerritoryKey` int(11) NOT NULL,
  `Region` varchar(100) NOT NULL,
  `Country` varchar(100) NOT NULL,
  `Continent` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `calendar`
--
ALTER TABLE `calendar`
  ADD PRIMARY KEY (`Date`);

--
-- Índices para tabela `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`ProductCategoryKey`);

--
-- Índices para tabela `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`CustomerKey`);

--
-- Índices para tabela `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductKey`),
  ADD KEY `ProductSubcategoryKey` (`ProductSubcategoryKey`);

--
-- Índices para tabela `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`SaleKey`),
  ADD KEY `ProductKey` (`ProductKey`),
  ADD KEY `CustomerKey` (`CustomerKey`),
  ADD KEY `TerritoryKey` (`TerritoryKey`);

--
-- Índices para tabela `subcategories`
--
ALTER TABLE `subcategories`
  ADD PRIMARY KEY (`ProductSubcategoryKey`),
  ADD KEY `subcategories_ibfk_1` (`ProductCategoryKey`);

--
-- Índices para tabela `territories`
--
ALTER TABLE `territories`
  ADD PRIMARY KEY (`SalesTerritoryKey`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `customers`
--
ALTER TABLE `customers`
  MODIFY `CustomerKey` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `products`
--
ALTER TABLE `products`
  MODIFY `ProductKey` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `sales`
--
ALTER TABLE `sales`
  MODIFY `SaleKey` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `subcategories`
--
ALTER TABLE `subcategories`
  MODIFY `ProductSubcategoryKey` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `territories`
--
ALTER TABLE `territories`
  MODIFY `SalesTerritoryKey` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`ProductSubcategoryKey`) REFERENCES `subcategories` (`ProductSubcategoryKey`);

--
-- Limitadores para a tabela `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`ProductKey`) REFERENCES `products` (`ProductKey`),
  ADD CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`CustomerKey`) REFERENCES `customers` (`CustomerKey`),
  ADD CONSTRAINT `sales_ibfk_3` FOREIGN KEY (`TerritoryKey`) REFERENCES `territories` (`SalesTerritoryKey`);

--
-- Limitadores para a tabela `subcategories`
--
ALTER TABLE `subcategories`
  ADD CONSTRAINT `subcategories_ibfk_1` FOREIGN KEY (`ProductCategoryKey`) REFERENCES `categories` (`ProductCategoryKey`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
