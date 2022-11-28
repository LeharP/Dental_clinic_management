-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 03:13 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: ` dental_clinic_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment_556`
--

CREATE TABLE `appointment_556` (
  `Appointment_type` varchar(40) NOT NULL,
  `Date_of_Appointment` date NOT NULL,
  `Patient_ID` varchar(10) NOT NULL,
  `End_time` varchar(40) NOT NULL,
  `Appointment_ID` varchar(10) NOT NULL,
  `Start_time` varchar(40) NOT NULL,
  `Doctor_ID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointment_556`
--

INSERT INTO `appointment_556` (`Appointment_type`, `Date_of_Appointment`, `Patient_ID`, `End_time`, `Appointment_ID`, `Start_time`, `Doctor_ID`) VALUES
('Root Canal', '2022-11-27', 'P01', '18:00', 'ID007', '17:30', 'D01'),
('Cleaning', '2022-11-27', 'P03', '19:00', 'ID008', '18:30', 'D03'),
('Bridge Fitting', '2022-11-28', 'P05', '18:30', 'ID009', '17:30', 'D04'),
('Braces', '2022-11-29', 'P02', '20:00', 'ID010', '18:00', 'D02'),
('Wisdom Tooth Removal', '2022-11-29', 'P08', '19:15', 'ID011', '18:30', 'D01'),
('Dental Implants', '2022-11-30', 'P06', '21:00', 'ID012', '19:00', 'D01');

-- --------------------------------------------------------

--
-- Table structure for table `billing_556`
--

CREATE TABLE `billing_556` (
  `Bill_ID` varchar(10) NOT NULL,
  `Total_amount` int(10) NOT NULL,
  `Payment_Type` varchar(10) NOT NULL,
  `Patient_ID` varchar(10) NOT NULL,
  `Payment_Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing_556`
--

INSERT INTO `billing_556` (`Bill_ID`, `Total_amount`, `Payment_Type`, `Patient_ID`, `Payment_Status`) VALUES
('BILL01', 12000, 'Card', 'P04', 'Pending'),
('BILL02', 75000, 'Cash', 'P03', 'Paid'),
('BILL03', 37000, 'UPI', 'P01', 'Pending'),
('BILL04', 78000, 'Cash', 'P02', 'Paid'),
('BILL05', 69000, 'Card', 'P08', 'Pending'),
('BILL06', 4300, 'UPI', 'P01', 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_556`
--

CREATE TABLE `doctor_556` (
  `Doctor_ID` varchar(10) NOT NULL,
  `Job_type` varchar(20) NOT NULL,
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `Pincode` int(6) NOT NULL,
  `Annual_salary` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor_556`
--

INSERT INTO `doctor_556` (`Doctor_ID`, `Job_type`, `First_Name`, `Last_Name`, `Street`, `Pincode`, `Annual_salary`) VALUES
('D01', 'Endodontist', 'Kiran', 'Kumar', 'Jayanagar', 560041, 1000000),
('D02', 'Orthodontist', 'Nithyaja', 'Kiran', 'JP Nagar', 560072, 900000),
('D03', 'Pedodontist', 'Preetham', 'Shetty', 'BDA complex', 560023, 690000),
('D04', 'Prosthodontist', 'Hari', 'Prasad', 'Rajajinagar', 560056, 690000),
('D05', 'Oral Pathologist', 'Karthik', 'Sharma', 'Uttrahalli', 560021, 700000);

-- --------------------------------------------------------

--
-- Table structure for table `patient_556`
--

CREATE TABLE `patient_556` (
  `Address` varchar(50) NOT NULL,
  `DOB` date NOT NULL,
  `Patient_ID` varchar(10) NOT NULL,
  `First_Name` varchar(20) NOT NULL,
  `Last_Name` varchar(20) NOT NULL,
  `Gender` varchar(1) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_556`
--

INSERT INTO `patient_556` (`Address`, `DOB`, `Patient_ID`, `First_Name`, `Last_Name`, `Gender`, `Email`, `Phone`) VALUES
('123 ABC', '1970-10-11', 'P01', 'Sanjita', 'Chandan', 'F', 'abc@xyz', 8296462187),
('234 BCD', '1973-10-12', 'P02', 'Lehar', 'Pothugunta', 'M', 'def@abc', 8296422182),
('345 CDE', '1973-09-13', 'P03', 'Shaarvari', 'Kiran', 'F', 'efg@xyz', 8298462187),
('456 DEF', '1973-09-14', 'P04', 'Shyam', 'Krishna', 'M', 'hij@abc', 9296462185),
('567 EFG', '1987-11-17', 'P05', 'Mohnish', 'Choudary', 'M', 'klm@xyz', 9276462183),
('678 FGH', '1989-08-19', 'P06', 'Devika', 'Kiran', 'F', 'nop@abc', 8292342187),
('789 GHI', '1999-03-10', 'P07', 'Kiran', 'Kumar', 'M', 'qrs@xyz', 9236262187),
('890 HIJ', '2002-10-24', 'P08', 'Nithya', 'Kiran', 'F', 'tuv@abc', 9223465187),
('901 IJK', '2003-03-08', 'P09', 'Girija', 'Merkaje', 'F', 'uvw@xyz', 9229748333),
('012 JKL', '2002-08-11', 'P10', 'Drupad', 'Bhandary', 'M', 'owo@abc', 8296462234);

-- --------------------------------------------------------

--
-- Table structure for table `review_556`
--

CREATE TABLE `review_556` (
  `Treatment_description` varchar(100) NOT NULL,
  `Date_of_review` date NOT NULL,
  `Cleanliness` int(2) NOT NULL,
  `Communication` int(2) NOT NULL,
  `Professionalism` int(2) NOT NULL,
  `Review_ID` varchar(7) NOT NULL,
  `Treatment_ID` varchar(10) NOT NULL,
  `Doctor_ID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `review_556`
--

INSERT INTO `review_556` (`Treatment_description`, `Date_of_review`, `Cleanliness`, `Communication`, `Professionalism`, `Review_ID`, `Treatment_ID`, `Doctor_ID`) VALUES
('Got a Root Canal Treatment', '0000-00-00', 8, 7, 6, 'R01', 'TID001', 'D01 '),
('Got a Bridge fixing treatment', '0000-00-00', 9, 5, 4, 'R02', 'TID002', 'D04 '),
('Got a Root Canal Treatment', '0000-00-00', 10, 9, 10, 'R03', 'TID001', 'D01 '),
('Got an Implant Treatment', '0000-00-00', 4, 8, 8, 'R04', 'TID003', 'D01 '),
('Got a Cleaning done', '0000-00-00', 5, 7, 7, 'R05', 'TID004', 'D03 '),
('Got my braces fixed', '0000-00-00', 9, 10, 8, 'R06', 'TID005', 'D02 ');

-- --------------------------------------------------------

--
-- Table structure for table `treatment_556`
--

CREATE TABLE `treatment_556` (
  `Treatment_ID` varchar(10) NOT NULL,
  `Tooth` int(4) NOT NULL,
  `Medication` varchar(50) DEFAULT NULL,
  `Patient_ID` varchar(10) NOT NULL,
  `Appointment_ID` varchar(10) NOT NULL,
  `Doctor_ID` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `treatment_556`
--

INSERT INTO `treatment_556` (`Treatment_ID`, `Tooth`, `Medication`, `Patient_ID`, `Appointment_ID`, `Doctor_ID`) VALUES
('TID001', 23, 'Midazolam', 'P01', 'ID007', 'D01'),
('TID002', 999, NULL, 'P05', 'ID009', 'D04'),
('TID003', 33, 'Anesthesia', 'P06', 'ID012', 'D01'),
('TID004', 21, NULL, 'P03', 'ID008', 'D03'),
('TID005', 999, NULL, 'P02', 'ID010', 'D02'),
('TID006', 24, 'Ibuprofen', 'P08', 'ID011', 'D01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment_556`
--
ALTER TABLE `appointment_556`
  ADD PRIMARY KEY (`Appointment_ID`),
  ADD KEY `Patient_ID` (`Patient_ID`),
  ADD KEY `Doctor_ID` (`Doctor_ID`);

--
-- Indexes for table `billing_556`
--
ALTER TABLE `billing_556`
  ADD PRIMARY KEY (`Bill_ID`),
  ADD KEY `Patient_ID` (`Patient_ID`);

--
-- Indexes for table `doctor_556`
--
ALTER TABLE `doctor_556`
  ADD PRIMARY KEY (`Doctor_ID`);

--
-- Indexes for table `patient_556`
--
ALTER TABLE `patient_556`
  ADD PRIMARY KEY (`Patient_ID`);

--
-- Indexes for table `review_556`
--
ALTER TABLE `review_556`
  ADD PRIMARY KEY (`Review_ID`),
  ADD KEY `Treatment_ID` (`Treatment_ID`),
  ADD KEY `Doctor_ID` (`Doctor_ID`);

--
-- Indexes for table `treatment_556`
--
ALTER TABLE `treatment_556`
  ADD PRIMARY KEY (`Treatment_ID`),
  ADD KEY `Patient_ID` (`Patient_ID`),
  ADD KEY `Appointment_ID` (`Appointment_ID`),
  ADD KEY `Doctor_ID` (`Doctor_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment_556`
--
ALTER TABLE `appointment_556`
  ADD CONSTRAINT `appointment_556_ibfk_1` FOREIGN KEY (`Patient_ID`) REFERENCES `patient_556` (`Patient_ID`),
  ADD CONSTRAINT `appointment_556_ibfk_2` FOREIGN KEY (`Doctor_ID`) REFERENCES `doctor_556` (`Doctor_ID`);

--
-- Constraints for table `billing_556`
--
ALTER TABLE `billing_556`
  ADD CONSTRAINT `billing_556_ibfk_1` FOREIGN KEY (`Patient_ID`) REFERENCES `patient_556` (`Patient_ID`);

--
-- Constraints for table `review_556`
--
ALTER TABLE `review_556`
  ADD CONSTRAINT `review_556_ibfk_1` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment_556` (`Treatment_ID`),
  ADD CONSTRAINT `review_556_ibfk_2` FOREIGN KEY (`Doctor_ID`) REFERENCES `doctor_556` (`Doctor_ID`);

--
-- Constraints for table `treatment_556`
--
ALTER TABLE `treatment_556`
  ADD CONSTRAINT `treatment_556_ibfk_1` FOREIGN KEY (`Patient_ID`) REFERENCES `patient_556` (`Patient_ID`),
  ADD CONSTRAINT `treatment_556_ibfk_2` FOREIGN KEY (`Appointment_ID`) REFERENCES `appointment_556` (`Appointment_ID`),
  ADD CONSTRAINT `treatment_556_ibfk_3` FOREIGN KEY (`Doctor_ID`) REFERENCES `doctor_556` (`Doctor_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
