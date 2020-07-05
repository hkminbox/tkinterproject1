-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 09, 2020 at 09:27 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database1`
--

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `Id` int(11) NOT NULL,
  `Name` char(40) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Sex` enum('Male','Female') DEFAULT NULL,
  `Phone` bigint(20) DEFAULT NULL,
  `Blood group` enum('A','B','AB','O') DEFAULT NULL,
  `Rh` enum('Positive','Negative') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`Id`, `Name`, `Age`, `Sex`, `Phone`, `Blood group`, `Rh`) VALUES
(1, 'Person1', 18, 'Male', 9123450000, 'A', 'Positive'),
(2, 'Person2', 21, 'Male', 9123450001, 'B', 'Positive'),
(3, 'Person3', 18, 'Female', 9123450002, 'AB', 'Negative'),
(4, 'Person4', 21, 'Male', 9123450003, 'B', 'Negative'),
(5, 'Person5', 18, 'Female', 9123450004, 'A', 'Positive'),
(6, 'Person6', 21, 'Male', 9123450005, 'B', 'Negative'),
(7, 'Person7', 18, 'Female', 9123450006, 'AB', 'Positive'),
(8, 'Person8', 45, 'Male', 9123450007, 'AB', 'Negative'),
(9, 'Person9', 44, 'Female', 9123450008, 'AB', 'Positive'),
(10, 'Person10', 18, 'Male', 9123450009, 'A', 'Negative'),
(11, 'Person11', 21, 'Female', 9123450010, 'A', 'Positive'),
(12, 'Person12', 45, 'Male', 9123450011, 'B', 'Negative'),
(13, 'Person13', 46, 'Female', 9123450012, 'AB', 'Positive'),
(14, 'Person14', 21, 'Male', 9123450013, 'A', 'Negative'),
(15, 'Person15', 18, 'Male', 9123450014, 'AB', 'Positive'),
(16, 'Person16', 21, 'Female', 9123450015, 'A', 'Negative'),
(17, 'Person17', 18, 'Female', 9123450016, 'B', 'Negative'),
(18, 'Person18', 29, 'Male', 9123450017, 'AB', 'Positive'),
(19, 'Person19', 21, 'Female', 9123450018, 'A', 'Negative'),
(20, 'Person20', 18, 'Female', 9123450019, 'AB', 'Positive'),
(21, 'Person21', 35, 'Female', 9123450020, 'A', 'Negative'),
(22, 'Person22', 21, 'Female', 9123450021, 'B', 'Negative'),
(23, 'Person23', 21, 'Female', 9123450022, 'AB', 'Positive'),
(24, 'Person24', 21, 'Male', 9123450023, 'AB', 'Positive'),
(25, 'Person25', 18, 'Female', 9123450024, 'A', 'Negative'),
(26, 'Person26', 44, 'Male', 9123450025, 'B', 'Positive'),
(27, 'Person27', 18, 'Female', 9123450026, 'AB', 'Negative'),
(28, 'Person28', 47, 'Female', 9123450027, 'A', 'Positive'),
(29, 'Person29', 18, 'Female', 9123450028, 'AB', 'Negative'),
(30, 'Person30', 33, 'Male', 9123450029, 'B', 'Positive'),
(31, 'Person31', 21, 'Female', 9123450030, 'AB', 'Negative'),
(32, 'Person32', 18, 'Male', 9123450031, 'AB', 'Positive'),
(33, 'Person33', 35, 'Female', 9123450032, 'B', 'Negative'),
(34, 'Person34', 45, 'Female', 9123450033, 'AB', 'Positive'),
(35, 'Person35', 21, 'Male', 9123450034, 'A', 'Negative'),
(36, 'Person36', 38, 'Male', 9123450035, 'B', 'Positive'),
(37, 'Person37', 18, 'Female', 9123450036, 'A', 'Negative'),
(38, 'Person38', 29, 'Female', 9123450037, 'AB', 'Positive'),
(39, 'Person39', 45, 'Male', 9123450038, 'AB', 'Positive'),
(40, 'Person40', 45, 'Male', 9123450039, 'A', 'Negative'),
(41, 'Person41', 18, 'Female', 9123450040, 'AB', 'Positive'),
(42, 'Person42', 21, 'Female', 9123450041, 'A', 'Negative'),
(43, 'Person43', 66, 'Male', 9123450042, 'B', 'Positive'),
(44, 'Person44', 36, 'Female', 9123450043, 'AB', 'Positive'),
(45, 'Person45', 18, 'Male', 9123450044, 'AB', 'Positive'),
(46, 'Person46', 21, 'Female', 9123450045, 'AB', 'Negative'),
(47, 'Person47', 44, 'Male', 9123450046, 'A', 'Positive'),
(48, 'Person48', 45, 'Male', 9123450047, 'AB', 'Negative'),
(49, 'Person49', 18, 'Male', 9123450048, 'B', 'Positive'),
(50, 'Person50', 21, 'Male', 9123450049, 'AB', 'Negative'),
(51, 'Person51', 45, 'Female', 9123450050, 'A', 'Positive'),
(52, 'Person52', 21, 'Female', 9123450051, 'AB', 'Negative'),
(53, 'Person53', 18, 'Female', 9123450052, 'AB', 'Positive'),
(54, 'Person54', 34, 'Male', 9123450053, 'B', 'Positive'),
(55, 'Person55', 35, 'Female', 9123450054, 'A', 'Positive'),
(56, 'Person56', 21, 'Male', 9123450055, 'B', 'Negative'),
(57, 'Person57', 21, 'Male', 9123450056, 'AB', 'Positive'),
(58, 'Person58', 36, 'Female', 9123450057, 'A', 'Negative'),
(59, 'Person59', 37, 'Female', 9123450058, 'A', 'Negative'),
(60, 'Person60', 21, 'Female', 9123450059, 'AB', 'Positive'),
(61, 'Person61', 18, 'Female', 9123450060, 'B', 'Negative'),
(62, 'Person62', 21, 'Female', 9123450061, 'A', 'Negative'),
(63, 'Person63', 38, 'Female', 9123450062, 'AB', 'Negative'),
(64, 'Person64', 21, 'Female', 9123450063, 'B', 'Positive'),
(65, 'Person65', 18, 'Male', 9123450064, 'A', 'Positive'),
(66, 'Person66', 39, 'Male', 9123450065, 'AB', 'Positive'),
(67, 'Person67', 21, 'Male', 9123450066, 'A', 'Negative'),
(68, 'Person68', 21, 'Male', 9123450067, 'AB', 'Negative'),
(69, 'Person69', 45, 'Male', 9123450068, 'B', 'Negative'),
(70, 'Person70', 29, 'Male', 9123450069, 'AB', 'Positive');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
