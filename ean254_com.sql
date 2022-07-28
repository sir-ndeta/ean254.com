-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 26, 2022 at 02:37 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ean254.com`
--

-- --------------------------------------------------------

--
-- Table structure for table `Admin`
--

CREATE TABLE `Admin` (
  `EmpNO` int(11) NOT NULL,
  `Picture` varchar(200) NOT NULL,
  `Name` varchar(20) NOT NULL,
`email` varchar(50) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Rating` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Admin`
--

INSERT INTO `Admin` (`EmpNO`, `Picture`, `Name`, `Password`, `Rating`) VALUES
(1, 'https://sirndeta.pythonanywhere.com/static/image/Ean.jpg', 'Ean ', '1234567890', '6');

-- --------------------------------------------------------

--
-- Table structure for table `Assignments`
--

CREATE TABLE `Assignments` (
  `SN.` int(11) NOT NULL,
  `Client Name` varchar(50) NOT NULL,
  `Client Phone Number` varchar(10) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `Service` varchar(50) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `clientdetails`
--

CREATE TABLE `clientdetails` (
  `Name` varchar(50) NOT NULL,
  `Email` varchar(90) NOT NULL,
  `Phone Number` varchar(10) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clientdetails`
--

INSERT INTO `clientdetails` (`Name`, `Email`, `Phone Number`, `Password`) VALUES
('Kerry Ndeta', 'kerrynw95@gmail.com', '0770100344', '0770100344');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `SN.` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`SN.`, `image`, `Name`, `Description`, `price`) VALUES
(1, 'https://sirndeta.pythonanywhere.com/static/image/babyshoot.png', 'Babies Photography', '\'Have memories of your sweet little pumpkin that even when he grows old you still have memory of the innocent face. At Ean254 Photography we can make it happen', '200'),
(2, 'https://sirndeta.pythonanywhere.com/static/image/outside.jpg', 'Potraits', '2Hours photoshoot, indoor/outdoor. NO limit of outfit change. 20 final edited photos', '2500');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Admin`
--
ALTER TABLE `Admin`
  ADD PRIMARY KEY (`EmpNO`);

--
-- Indexes for table `Assignments`
--
ALTER TABLE `Assignments`
  ADD PRIMARY KEY (`SN.`);

--
-- Indexes for table `clientdetails`
--
ALTER TABLE `clientdetails`
  ADD PRIMARY KEY (`Password`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`SN.`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Admin`
--
ALTER TABLE `Admin`
  MODIFY `EmpNO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Assignments`
--
ALTER TABLE `Assignments`
  MODIFY `SN.` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `SN.` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
