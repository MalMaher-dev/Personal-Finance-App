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
DROP DATABASE IF EXISTS project;
CREATE DATABASE project;

USE project;



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
INSERT INTO `accountinfo` VALUES ('Dayton','Dawson',0.00,1122,'dDawson','Daytond','2026-03-21 21:16:25'),('John','Smith',29.99,1234,'jSmith','JohnS','2026-03-21 20:57:37'),('Mallory','Maher',21.95,5676,'mMaher','MalloryM','2026-05-03 11:47:16'),('Jane','Dow',876.64,9521,'jDow','JaneD','2026-03-21 20:57:37');
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
  `dateDone` date NOT NULL,
  `accountNumber` int(11) DEFAULT NULL,
  `transactionNumber` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) DEFAULT NULL,
  `retailer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`transactionNumber`),
  KEY `fk_accountNumber` (`accountNumber`),
  CONSTRAINT `fk_accountNumber` FOREIGN KEY (`accountNumber`) REFERENCES `accountinfo` (`accountNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES ('2026-04-19 21:26:00','2021-12-25',9521,1,199.99,'Amazon'),('2026-05-03 11:14:24','2000-08-19',9521,2,8.51,'Calvin Klein'),('2026-05-03 11:14:24','2006-10-26',9521,3,14.56,'Walmart'),('2026-05-03 11:14:24','2008-07-23',9521,4,69.94,'Aldi\'s'),('2026-05-03 11:17:04','2017-01-17',9521,5,10.91,'Calvin Klein'),('2026-05-03 11:17:04','2022-01-11',9521,6,59.47,'Aldi\'s'),('2026-05-03 11:17:04','2022-09-18',9521,7,23.93,'Amazon'),('2026-05-03 11:17:04','2004-07-09',9521,8,63.49,'Asda'),('2026-05-03 11:17:04','2019-12-25',9521,9,2.10,'Target'),('2026-05-03 11:17:04','2021-09-23',9521,10,38.78,'Costco'),('2026-05-03 11:17:04','2015-08-12',9521,11,2.50,'Amazon'),('2026-05-03 11:17:04','2003-07-11',9521,12,18.12,'Amazon'),('2026-05-03 11:17:04','2008-12-28',9521,13,6.73,'Calvin Klein'),('2026-05-03 11:17:04','2006-12-11',9521,14,20.83,'Amazon'),('2026-05-03 11:18:10','2013-03-01',9521,15,7.92,'Sam\'s Club'),('2026-05-03 11:18:10','2004-06-10',9521,16,13.78,'Aldi\'s'),('2026-05-03 11:18:10','2003-10-25',9521,17,61.42,'Walmart'),('2026-05-03 11:18:10','2020-11-16',9521,18,25.19,'Walmart'),('2026-05-03 11:18:10','2017-01-31',9521,19,48.62,'Costco'),('2026-05-03 11:18:10','2015-08-31',9521,20,27.27,'Target'),('2026-05-03 11:18:10','2024-01-02',9521,21,14.84,'Target'),('2026-05-03 11:18:10','2016-10-06',9521,22,46.52,'Amazon'),('2026-05-03 11:18:10','2022-01-25',9521,23,41.92,'Sam\'s Club'),('2026-05-03 11:18:10','2015-12-30',9521,24,49.30,'Target'),('2026-05-03 11:25:10','2015-01-22',1234,25,29.99,'Costco'),('2026-05-03 11:47:55','2023-02-13',5676,26,21.95,'Walmart');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `project`.`transactions_AFTER_INSERT` AFTER INSERT ON `transactions` FOR EACH ROW
BEGIN
	UPDATE accountinfo
    SET balance = balance + NEW.amount
    WHERE accountNumber = NEW.accountNumber;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `project`.`transactions_AFTER_UPDATE` AFTER UPDATE ON `transactions` FOR EACH ROW
BEGIN
	UPDATE accountinfo
    SET balance = balance - OLD.amount + NEW.amount
    WHERE accountNumber = NEW.accountNumber;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `project`.`transactions_AFTER_DELETE` AFTER DELETE ON `transactions` FOR EACH ROW
BEGIN
	UPDATE accountinfo
    SET balance = balance - OLD.amount
    WHERE accountNumber = OLD.accountNumber;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;


CREATE USER 'guest'@'%' IDENTIFIED BY 'psssword';
GRANT ALL PRIVILEGES ON project.* TO 'guest'@'%';
FLUSH PRIVILEGES;

-- Dump completed on 2026-05-04  9:46:07
