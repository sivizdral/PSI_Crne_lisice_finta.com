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
-- Table structure for table `article`
--

DROP TABLE IF EXISTS `article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `article` (
  `idArticle` int NOT NULL AUTO_INCREMENT,
  `Image` varchar(100) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Value` int NOT NULL,
  `Text` varchar(255) NOT NULL,
  `idArticleType` int NOT NULL,
  PRIMARY KEY (`idArticle`),
  KEY `article_idArticleType_76800096_fk_articletype_idArticleType` (`idArticleType`),
  CONSTRAINT `article_idArticleType_76800096_fk_articletype_idArticleType` FOREIGN KEY (`idArticleType`) REFERENCES `articletype` (`idArticleType`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `article`
--

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;
INSERT INTO `article` VALUES (1,'images/1._FC_Union_Berlin.svg','1. FC Union Berlin',50,'Bundesliga',5),(2,'images/1._FSV_Mainz_05.svg','1. FSV Mainz 05',60,'Bundesliga',5),(3,'images/Arminia_Bielefeld.svg','Arminia Bielefeld',50,'Bundesliga',5),(4,'images/Bayer_04_Leverkusen.svg','Bayer 04 Leverkusen',150,'Bundesliga',5),(5,'images/Borussia_Dortmund.svg','Borussia Dortmund',250,'Bundesliga',5),(6,'images/Borussia_Mgladbach.svg','Borussia M\'gladbach',150,'Bundesliga',5),(7,'images/Eintracht_Frankfurt.svg','Eintracht Frankfurt',60,'Bundesliga',5),(8,'images/FC_Augsburg.svg','FC Augsburg',100,'Bundesliga',5),(9,'images/FC_Bayern_Munchen.svg','FC Bayern Munchen',350,'Bundesliga',5),(10,'images/FC_Koln.svg','FC Koln',100,'Bundesliga',5),(11,'images/Hertha_Berlin.svg','Hertha Berlin',80,'Bundesliga',5),(12,'images/RB_Leipzig.svg','RB Leipzig',100,'Bundesliga',5),(13,'images/SC_Freiburg.svg','SC Freiburg',90,'Bundesliga',5),(14,'images/SpVgg_Greuther_Furth.svg','SpVgg Greuther Furth',80,'Bundesliga',5),(15,'images/TSG_Hoffenheim.svg','TSG Hoffenheim',130,'Bundesliga',5),(16,'images/VfB_Stuttgart.svg','VfB Stuttgart',140,'Bundesliga',5),(17,'images/VfL_Bochum_1848.svg','VfL Bochum 1848',70,'Bundesliga',5),(18,'images/VfL_Wolfsburg.svg','VfL Wolfsburg',110,'Bundesliga',5),(19,'images/Atalanta.png','Atalanta',150,'Serie A',5),(20,'images/Bologna.png','Bologna',200,'Serie A',5),(21,'images/Cagliari.png','Cagliari',80,'Serie A',5),(22,'images/Empoli.png','Empoli',50,'Serie A',5),(23,'images/Fiorentina.png','Fiorentina',200,'Serie A',5),(24,'images/Genoa.png','Genoa',90,'Serie A',5),(25,'images/Hellas_Verona.png','Hellas Verona',60,'Serie A',5),(26,'images/Internazionale.png','Internazionale',120,'Serie A',5),(27,'images/Juventus.png','Juventus',300,'Serie A',5),(28,'images/Lazio.png','Lazio',130,'Serie A',5),(29,'images/Milan.png','Milan',140,'Serie A',5),(30,'images/Napoli.png','Napoli',160,'Serie A',5),(31,'images/Roma.png','Roma',110,'Serie A',5),(32,'images/Salernitana.png','Salernitana',40,'Serie A',5),(33,'images/Sampdoria.png','Sampdoria',90,'Serie A',5),(34,'images/Sassuolo_Calcio.png','Sassuolo Calcio',40,'Serie A',5),(35,'images/Spezia_Calcio.png','Spezia Calcio',60,'Serie A',5),(36,'images/Torino.png','Torino',110,'Serie A',5),(37,'images/Udinese_Calcio.png','Udinese Calcio',60,'Serie A',5),(38,'images/Venezia.png','Venezia',70,'Serie A',5),(39,'images/Argentina_Jersey.png','Argentina Jersey',200,'World Cup',4),(40,'images/Costa_Rica_Jersey.png','Costa Rica Jersey',100,'World Cup',4),(41,'images/Barcelona_Jersey.png','Barcelona Jersey',400,'La Liga',4),(42,'images/Messi_Old_Jersey.png','Messi Old Jersey',400,'La Liga',4),(43,'images/Griezmann_Jersey.png','Griezmann Jersey',300,'La Liga',4),(44,'images/Neymar_Jersey.png','Neymar Jersey',400,'Ligue 1',4);
/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 16:18:42
