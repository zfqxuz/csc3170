-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: csc3170
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `application`
--

DROP TABLE IF EXISTS `application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `application` (
  `app_id` int NOT NULL,
  `app_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `uid` int NOT NULL,
  `ename` varchar(255) DEFAULT NULL,
  `pname` varchar(255) DEFAULT NULL,
  `type_lv1` varchar(10) DEFAULT NULL,
  `type_lv2` varchar(10) DEFAULT NULL,
  `type_lv3` varchar(10) DEFAULT NULL,
  `text` mediumblob,
  PRIMARY KEY (`app_id`),
  KEY `uid` (`uid`),
  CONSTRAINT `application_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `ug1` (`uid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `cname` varchar(255) NOT NULL,
  `cid` int NOT NULL,
  `type` int NOT NULL,
  `employ_num` int DEFAULT NULL,
  `asset_size` int DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_own`
--

DROP TABLE IF EXISTS `company_own`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_own` (
  `app_id` int DEFAULT NULL,
  `id` int DEFAULT NULL,
  `comp_id` int DEFAULT NULL,
  KEY `app_id` (`app_id`),
  KEY `FK_ID` (`comp_id`),
  CONSTRAINT `company_own_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `result` (`app_id`) ON DELETE CASCADE,
  CONSTRAINT `FK_ID` FOREIGN KEY (`comp_id`) REFERENCES `company` (`cid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_own`
--

LOCK TABLES `company_own` WRITE;
/*!40000 ALTER TABLE `company_own` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_own` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `birthday` date NOT NULL,
  `add_country` varchar(255) DEFAULT NULL,
  `add_state` varchar(255) DEFAULT NULL,
  `add_city` varchar(255) DEFAULT NULL,
  `add_street` varchar(255) DEFAULT NULL,
  `career` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_own`
--

DROP TABLE IF EXISTS `personal_own`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_own` (
  `id` int DEFAULT NULL,
  `app_id` int DEFAULT NULL,
  KEY `app_id` (`app_id`),
  KEY `FK_PID` (`id`),
  CONSTRAINT `FK_PID` FOREIGN KEY (`id`) REFERENCES `person` (`id`) ON DELETE CASCADE,
  CONSTRAINT `personal_own_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `result` (`app_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_own`
--

LOCK TABLES `personal_own` WRITE;
/*!40000 ALTER TABLE `personal_own` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_own` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref`
--

DROP TABLE IF EXISTS `ref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ref` (
  `ref_id` int DEFAULT NULL,
  `pid` int DEFAULT NULL,
  KEY `pid` (`pid`),
  CONSTRAINT `ref_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `application` (`app_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref`
--

LOCK TABLES `ref` WRITE;
/*!40000 ALTER TABLE `ref` DISABLE KEYS */;
/*!40000 ALTER TABLE `ref` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reject_detail`
--

DROP TABLE IF EXISTS `reject_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reject_detail` (
  `app_id` int NOT NULL,
  `app_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` int NOT NULL,
  `reason_1` int NOT NULL,
  `reason_2` int NOT NULL,
  `reason_3` int NOT NULL,
  `ref_reason1` int NOT NULL,
  `ref_reason2` int NOT NULL,
  `ref_reason3` int NOT NULL,
  KEY `app_id` (`app_id`),
  CONSTRAINT `reject_detail_ibfk_1` FOREIGN KEY (`app_id`) REFERENCES `result` (`app_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reject_detail`
--

LOCK TABLES `reject_detail` WRITE;
/*!40000 ALTER TABLE `reject_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `reject_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `app_id` int NOT NULL,
  `app_date` timestamp(6) NOT NULL,
  `process_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `status_1` int DEFAULT NULL,
  `status_2` int DEFAULT NULL,
  `status_3` int DEFAULT NULL,
  `final_status` int DEFAULT NULL,
  `owner` varchar(255) DEFAULT NULL,
  `owner_type` int DEFAULT NULL,
  `ename` varchar(255) DEFAULT NULL,
  `pname` varchar(255) DEFAULT NULL,
  `grant_date` date DEFAULT NULL,
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ug1`
--

DROP TABLE IF EXISTS `ug1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ug1` (
  `uid` int NOT NULL,
  `pwd` int DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ug1`
--

LOCK TABLES `ug1` WRITE;
/*!40000 ALTER TABLE `ug1` DISABLE KEYS */;
/*!40000 ALTER TABLE `ug1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-02  1:10:20
