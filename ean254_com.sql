-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 02 aug 2022 kl 00:41
-- Serverversion: 10.4.24-MariaDB
-- PHP-version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `ean254.com`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `admin`
--

CREATE TABLE `admin` (
  `EmpNO` int(11) NOT NULL,
  `Picture` varchar(200) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Rating` varchar(3) NOT NULL,
  `Email` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `admin`
--

INSERT INTO `admin` (`EmpNO`, `Picture`, `Name`, `Password`, `Rating`, `Email`) VALUES
(1, 'https://sirndeta.pythonanywhere.com/static/image/Ean.jpg', 'Ean ', '1234567890', '6', 'ean254@gmail.com');

-- --------------------------------------------------------

--
-- Tabellstruktur `assignments`
--

CREATE TABLE `assignments` (
  `SN.` int(11) NOT NULL,
  `Client Name` varchar(50) NOT NULL,
  `Client Phone Number` varchar(10) NOT NULL,
  `Location` varchar(50) NOT NULL,
  `Service` varchar(50) NOT NULL,
  `Status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur `clientdetails`
--

CREATE TABLE `clientdetails` (
  `Name` varchar(50) NOT NULL,
  `email` varchar(90) NOT NULL,
  `pnumb` varchar(10) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Gender` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `clientdetails`
--

INSERT INTO `clientdetails` (`Name`, `email`, `pnumb`, `Password`, `Gender`) VALUES
('Kerry Ndeta', 'kerrynw95@gmail.com', '0770100344', '0770100344', '');

-- --------------------------------------------------------

--
-- Tabellstruktur `services`
--

CREATE TABLE `services` (
  `SN` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `services`
--

INSERT INTO `services` (`SN`, `image`, `Name`, `Description`, `price`) VALUES
(1, 'https://sirndeta.pythonanywhere.com/static/image/babyshoot.png', 'Babies Photography', '\'Have memories of your sweet little pumpkin that even when he grows old you still have memory of the innocent face. At Ean254 Photography we can make it happen', '200'),
(2, 'https://sirndeta.pythonanywhere.com/static/image/outside.jpg', 'Potraits', '2Hours photoshoot, indoor/outdoor. NO limit of outfit change. 20 final edited photos', '2500');

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`EmpNO`);

--
-- Index för tabell `assignments`
--
ALTER TABLE `assignments`
  ADD PRIMARY KEY (`SN.`);

--
-- Index för tabell `clientdetails`
--
ALTER TABLE `clientdetails`
  ADD PRIMARY KEY (`Password`);

--
-- Index för tabell `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`SN`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `admin`
--
ALTER TABLE `admin`
  MODIFY `EmpNO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT för tabell `assignments`
--
ALTER TABLE `assignments`
  MODIFY `SN.` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT för tabell `services`
--
ALTER TABLE `services`
  MODIFY `SN` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
