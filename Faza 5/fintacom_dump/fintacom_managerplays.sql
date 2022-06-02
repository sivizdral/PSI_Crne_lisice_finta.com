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
-- Table structure for table `managerplays`
--

DROP TABLE IF EXISTS `managerplays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `managerplays` (
  `idManagerPlays` int NOT NULL AUTO_INCREMENT,
  `idManagerTeam` int NOT NULL,
  `idPlayer` int NOT NULL,
  PRIMARY KEY (`idManagerPlays`),
  KEY `managerplays_idManagerTeam_e97f50ea_fk_managerteam_idManagerTeam` (`idManagerTeam`),
  KEY `managerplays_idPlayer_5d0706ae_fk_player_idPlayer` (`idPlayer`),
  CONSTRAINT `managerplays_idManagerTeam_e97f50ea_fk_managerteam_idManagerTeam` FOREIGN KEY (`idManagerTeam`) REFERENCES `managerteam` (`idManagerTeam`),
  CONSTRAINT `managerplays_idPlayer_5d0706ae_fk_player_idPlayer` FOREIGN KEY (`idPlayer`) REFERENCES `player` (`idPlayer`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managerplays`
--

LOCK TABLES `managerplays` WRITE;
/*!40000 ALTER TABLE `managerplays` DISABLE KEYS */;
INSERT INTO `managerplays` VALUES (14,2,14),(15,2,15),(16,2,16),(17,2,17),(18,2,18),(19,2,19),(20,2,20),(21,2,21),(22,2,22),(23,2,23),(24,2,24),(25,3,25),(26,3,26),(27,3,27),(28,3,28),(29,3,29),(30,3,30),(31,3,31),(32,3,32),(33,3,33),(34,4,34),(35,4,35),(36,4,36),(37,4,37),(38,4,38),(39,4,39),(40,4,40),(41,4,41),(42,4,42),(43,7,43),(44,7,44),(45,7,45),(46,7,46),(47,7,47),(48,7,48),(49,7,49),(50,7,50),(51,7,51),(52,7,52),(53,7,53),(55,10,55),(56,10,56),(57,10,57),(58,10,58),(59,10,59),(60,10,60),(61,10,61),(62,10,62),(63,10,63),(64,10,64),(65,10,65),(67,3,67),(68,3,68);
/*!40000 ALTER TABLE `managerplays` ENABLE KEYS */;
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
