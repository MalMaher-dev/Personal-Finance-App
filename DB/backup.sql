-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accountinfo`
--

DROP TABLE IF EXISTS `accountinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountinfo` (
  `firstName` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL,
  `accountNumber` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `dateCreated` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`accountNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountinfo`
--

LOCK TABLES `accountinfo` WRITE;
/*!40000 ALTER TABLE `accountinfo` DISABLE KEYS */;
INSERT INTO `accountinfo` VALUES ('Dayton','Dawson',0.00,1122,'dDawson','Daytond','2026-03-21 21:16:25'),('John','Smith',40.89,1234,'jSmith','JohnS','2026-03-21 20:57:37'),('Jane','Dow',209.82,9521,'jDow','JaneD','2026-03-21 20:57:37');
/*!40000 ALTER TABLE `accountinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `dateCreated` datetime DEFAULT current_timestamp(),
  `accountNumber` int(11) DEFAULT NULL,
  `transactionNumber` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) DEFAULT NULL,
  `retailer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`transactionNumber`),
  KEY `fk_accountNumber` (`accountNumber`),
  CONSTRAINT `fk_accountNumber` FOREIGN KEY (`accountNumber`) REFERENCES `accountinfo` (`accountNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES ('2026-03-21 20:57:49',9521,1,26.66,'Walmart'),('2026-03-21 20:57:49',9521,2,73.21,'Calvin Klein'),('2026-03-21 20:57:49',1234,3,21.15,'Costco'),('2026-03-21 20:57:49',9521,4,11.45,'Walmart'),('2026-03-21 20:57:49',9521,5,81.33,'Target'),('2026-03-21 20:57:49',9521,6,10.41,'Costco'),('2026-03-21 20:57:49',1234,7,2.23,'Calvin Klein'),('2026-03-21 20:57:49',9521,8,6.76,'Amazon'),('2026-03-21 20:57:49',1234,9,9.97,'Costco'),('2026-03-21 20:57:49',1234,10,7.54,'Amazon'),('2026-03-21 21:02:45',1234,11,5.67,'Target'),('2026-03-21 21:02:45',9521,12,47.87,'Target'),('2026-03-21 21:02:45',9521,13,33.52,'Walmart'),('2026-03-21 21:02:45',1234,14,1.57,'Amazon'),('2026-03-21 21:02:45',9521,15,15.58,'Calvin Klein'),('2026-03-21 21:02:45',1234,16,7.53,'Walmart'),('2026-03-21 21:02:45',1234,17,8.76,'Calvin Klein'),('2026-03-21 21:02:45',1234,18,61.90,'Target'),('2026-03-21 21:02:45',1234,19,45.28,'Walmart'),('2026-03-21 21:02:45',1234,20,1.15,'Amazon');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-23  2:48:12
