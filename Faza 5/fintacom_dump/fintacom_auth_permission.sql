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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add article',7,'add_article'),(26,'Can change article',7,'change_article'),(27,'Can delete article',7,'delete_article'),(28,'Can view article',7,'view_article'),(29,'Can add articletype',8,'add_articletype'),(30,'Can change articletype',8,'change_articletype'),(31,'Can delete articletype',8,'delete_articletype'),(32,'Can view articletype',8,'view_articletype'),(33,'Can add championship',9,'add_championship'),(34,'Can change championship',9,'change_championship'),(35,'Can delete championship',9,'delete_championship'),(36,'Can view championship',9,'view_championship'),(37,'Can add league',10,'add_league'),(38,'Can change league',10,'change_league'),(39,'Can delete league',10,'delete_league'),(40,'Can view league',10,'view_league'),(41,'Can add team',11,'add_team'),(42,'Can change team',11,'change_team'),(43,'Can delete team',11,'delete_team'),(44,'Can view team',11,'view_team'),(45,'Can add player',12,'add_player'),(46,'Can change player',12,'change_player'),(47,'Can delete player',12,'delete_player'),(48,'Can view player',12,'view_player'),(49,'Can add participates',13,'add_participates'),(50,'Can change participates',13,'change_participates'),(51,'Can delete participates',13,'delete_participates'),(52,'Can view participates',13,'view_participates'),(53,'Can add owns',14,'add_owns'),(54,'Can change owns',14,'change_owns'),(55,'Can delete owns',14,'delete_owns'),(56,'Can view owns',14,'view_owns'),(57,'Can add managerteam',15,'add_managerteam'),(58,'Can change managerteam',15,'change_managerteam'),(59,'Can delete managerteam',15,'delete_managerteam'),(60,'Can view managerteam',15,'view_managerteam'),(61,'Can add managerplays',16,'add_managerplays'),(62,'Can change managerplays',16,'change_managerplays'),(63,'Can delete managerplays',16,'delete_managerplays'),(64,'Can view managerplays',16,'view_managerplays'),(65,'Can add fixture',17,'add_fixture'),(66,'Can change fixture',17,'change_fixture'),(67,'Can delete fixture',17,'delete_fixture'),(68,'Can view fixture',17,'view_fixture'),(69,'Can add comment',18,'add_comment'),(70,'Can change comment',18,'change_comment'),(71,'Can delete comment',18,'delete_comment'),(72,'Can view comment',18,'view_comment'),(73,'Can add championshipmanagerteam',19,'add_championshipmanagerteam'),(74,'Can change championshipmanagerteam',19,'change_championshipmanagerteam'),(75,'Can delete championshipmanagerteam',19,'delete_championshipmanagerteam'),(76,'Can view championshipmanagerteam',19,'view_championshipmanagerteam'),(77,'Can add role',20,'add_role'),(78,'Can change role',20,'change_role'),(79,'Can delete role',20,'delete_role'),(80,'Can view role',20,'view_role');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
