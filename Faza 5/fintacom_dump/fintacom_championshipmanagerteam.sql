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
-- Table structure for table `championshipmanagerteam`
--

DROP TABLE IF EXISTS `championshipmanagerteam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `championshipmanagerteam` (
  `idChampionshipManagerTeam` int NOT NULL AUTO_INCREMENT,
  `Rank` int NOT NULL,
  `idChampionship` int NOT NULL,
  `idManagerTeam` int NOT NULL,
  PRIMARY KEY (`idChampionshipManagerTeam`),
  KEY `championshipmanagert_idChampionship_9c7f1060_fk_champions` (`idChampionship`),
  KEY `championshipmanagert_idManagerTeam_3475feda_fk_managerte` (`idManagerTeam`),
  CONSTRAINT `championshipmanagert_idChampionship_9c7f1060_fk_champions` FOREIGN KEY (`idChampionship`) REFERENCES `championship` (`idChampionship`),
  CONSTRAINT `championshipmanagert_idManagerTeam_3475feda_fk_managerte` FOREIGN KEY (`idManagerTeam`) REFERENCES `managerteam` (`idManagerTeam`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `championshipmanagerteam`
--

LOCK TABLES `championshipmanagerteam` WRITE;
/*!40000 ALTER TABLE `championshipmanagerteam` DISABLE KEYS */;
INSERT INTO `championshipmanagerteam` VALUES (2,-1,3,2);
/*!40000 ALTER TABLE `championshipmanagerteam` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 16:18:41
