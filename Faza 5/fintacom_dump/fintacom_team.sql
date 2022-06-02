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
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `idTeam` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Country` varchar(255) NOT NULL,
  `Photo` varchar(255) NOT NULL,
  `Id` int NOT NULL,
  PRIMARY KEY (`idTeam`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(2,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(3,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(4,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(5,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(6,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(7,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(8,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(9,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(10,'Bayern Munich','','https://media.api-sports.io/football/teams/157.png',157),(11,'Hamburger SV','','https://media.api-sports.io/football/teams/175.png',175),(12,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(13,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(14,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(15,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(16,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(17,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(18,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(19,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(20,'Barcelona','','https://media.api-sports.io/football/teams/529.png',529),(21,'Manchester United','','https://media.api-sports.io/football/teams/33.png',33),(22,'Real Madrid','','https://media.api-sports.io/football/teams/541.png',541),(23,'Borussia Dortmund','','https://media.api-sports.io/football/teams/165.png',165),(24,'Chelsea','','https://media.api-sports.io/football/teams/49.png',49),(25,'Real Madrid','','https://media.api-sports.io/football/teams/541.png',541),(26,'Manchester City','','https://media.api-sports.io/football/teams/50.png',50),(27,'FK Crvena Zvezda','','https://media.api-sports.io/football/teams/598.png',598),(28,'FK Crvena Zvezda','','https://media.api-sports.io/football/teams/598.png',598),(29,'Arsenal','','https://media.api-sports.io/football/teams/42.png',42),(30,'FK Crvena Zvezda','','https://media.api-sports.io/football/teams/598.png',598),(31,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(32,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(33,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(34,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(35,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(36,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(37,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(38,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(39,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(40,'Liverpool','','https://media.api-sports.io/football/teams/40.png',40),(42,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(43,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(44,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(45,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(46,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(47,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(48,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(49,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(50,'AC Milan','','https://media.api-sports.io/football/teams/489.png',489),(51,'Borussia Dortmund','','https://media.api-sports.io/football/teams/165.png',165),(52,'Paris Saint Germain','','https://media.api-sports.io/football/teams/85.png',85),(54,'FK Crvena Zvezda','','https://media.api-sports.io/football/teams/598.png',598),(55,'Manchester United','','https://media.api-sports.io/football/teams/33.png',33);
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 16:18:44
