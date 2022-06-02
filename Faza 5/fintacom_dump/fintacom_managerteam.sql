-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: fintacom
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `managerteam`
--

DROP TABLE IF EXISTS `managerteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `managerteam` (
  `idManagerTeam` int NOT NULL AUTO_INCREMENT,
  `Offence` int NOT NULL,
  `Defence` int NOT NULL,
  `Value` int NOT NULL,
  `Overall` int NOT NULL,
  `Rank` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `username` bigint NOT NULL,
  `Registered` int NOT NULL DEFAULT '0',
  `Count` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`idManagerTeam`),
  KEY `managerteam_username_3a4f9040_fk_user_id` (`username`),
  CONSTRAINT `managerteam_username_3a4f9040_fk_user_id` FOREIGN KEY (`username`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managerteam`
--

LOCK TABLES `managerteam` WRITE;
/*!40000 ALTER TABLE `managerteam` DISABLE KEYS */;
INSERT INTO `managerteam` VALUES (2,47,269,1961,301,0,'dr_bojic',14,1,11),(3,113,258,1893,289,0,'tasha',6,1,11),(4,188,302,1613,404,0,'zodra',10,0,9),(5,0,0,0,0,0,'ivan',3,0,0),(6,0,0,0,0,0,'berke',8,0,0),(7,104,238,1812,311,0,'dp',9,1,11),(8,0,0,0,0,0,'kolja',11,0,0),(9,0,0,0,0,0,'lekr',12,0,0),(10,125,294,2142,380,0,'ogriz',13,1,11);
/*!40000 ALTER TABLE `managerteam` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 16:18:45
