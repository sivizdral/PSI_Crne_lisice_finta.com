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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-06-01 10:21:16.767289','39','Article object (39)',1,'[{\"added\": {}}]',7,3),(2,'2022-06-01 10:21:53.814790','40','Article object (40)',1,'[{\"added\": {}}]',7,3),(3,'2022-06-01 10:22:14.483666','41','Article object (41)',1,'[{\"added\": {}}]',7,3),(4,'2022-06-01 10:22:38.078570','42','Article object (42)',1,'[{\"added\": {}}]',7,3),(5,'2022-06-01 10:24:31.885041','43','Article object (43)',1,'[{\"added\": {}}]',7,3),(6,'2022-06-01 10:24:55.845386','44','Article object (44)',1,'[{\"added\": {}}]',7,3),(7,'2022-06-02 13:03:06.118365','1','default',1,'[{\"added\": {}}]',3,3),(8,'2022-06-02 13:06:28.713691','1','default',3,'',3,3),(9,'2022-06-02 13:07:56.631770','2','default',1,'[{\"added\": {}}]',3,3),(10,'2022-06-02 13:09:01.336277','3','moderator',1,'[{\"added\": {}}]',3,3),(11,'2022-06-02 13:09:31.842015','5','abc',3,'',6,3),(12,'2022-06-02 13:09:36.012171','4','iki',3,'',6,3),(13,'2022-06-02 13:09:40.367725','2','ivancvetic',3,'',6,3),(17,'2022-06-02 13:10:40.535169','1','Championshipmanagerteam object (1)',3,'',19,3),(18,'2022-06-02 13:10:45.303580','1','Championship object (1)',3,'',9,3),(19,'2022-06-02 13:10:48.117357','2','Championship object (2)',3,'',9,3),(21,'2022-06-02 13:11:10.781124','12','Managerplays object (12)',3,'',16,3),(22,'2022-06-02 13:11:13.942153','11','Managerplays object (11)',3,'',16,3),(23,'2022-06-02 13:11:16.443205','10','Managerplays object (10)',3,'',16,3),(24,'2022-06-02 13:11:19.096525','9','Managerplays object (9)',3,'',16,3),(25,'2022-06-02 13:11:21.676867','8','Managerplays object (8)',3,'',16,3),(26,'2022-06-02 13:11:24.415304','7','Managerplays object (7)',3,'',16,3),(27,'2022-06-02 13:11:27.164011','6','Managerplays object (6)',3,'',16,3),(28,'2022-06-02 13:11:29.865069','5','Managerplays object (5)',3,'',16,3),(29,'2022-06-02 13:11:32.852817','4','Managerplays object (4)',3,'',16,3),(30,'2022-06-02 13:11:35.704287','3','Managerplays object (3)',3,'',16,3),(31,'2022-06-02 13:11:43.206420','1','Managerteam object (1)',3,'',15,3),(33,'2022-06-02 13:12:13.522668','9','Owns object (9)',3,'',14,3),(34,'2022-06-02 13:12:16.685514','8','Owns object (8)',3,'',14,3),(35,'2022-06-02 13:12:19.603302','7','Owns object (7)',3,'',14,3),(36,'2022-06-02 13:12:29.626490','6','Owns object (6)',3,'',14,3),(37,'2022-06-02 13:12:29.634489','5','Owns object (5)',3,'',14,3),(38,'2022-06-02 13:12:29.641929','4','Owns object (4)',3,'',14,3),(39,'2022-06-02 13:12:29.648899','3','Owns object (3)',3,'',14,3),(40,'2022-06-02 13:12:29.655900','2','Owns object (2)',3,'',14,3),(41,'2022-06-02 13:12:29.661904','1','Owns object (1)',3,'',14,3),(42,'2022-06-02 13:12:59.670326','12','Team object (12)',3,'',11,3),(43,'2022-06-02 13:12:59.677324','11','Team object (11)',3,'',11,3),(44,'2022-06-02 13:12:59.682356','10','Team object (10)',3,'',11,3),(45,'2022-06-02 13:12:59.687326','9','Team object (9)',3,'',11,3),(46,'2022-06-02 13:12:59.691332','8','Team object (8)',3,'',11,3),(47,'2022-06-02 13:12:59.695344','7','Team object (7)',3,'',11,3),(48,'2022-06-02 13:12:59.699485','6','Team object (6)',3,'',11,3),(49,'2022-06-02 13:13:00.031971','5','Team object (5)',3,'',11,3),(50,'2022-06-02 13:13:00.036599','4','Team object (4)',3,'',11,3),(51,'2022-06-02 13:13:00.040137','3','Team object (3)',3,'',11,3),(52,'2022-06-02 13:13:14.398818','12','Player object (12)',3,'',12,3),(53,'2022-06-02 13:13:14.402815','11','Player object (11)',3,'',12,3),(54,'2022-06-02 13:13:14.407133','10','Player object (10)',3,'',12,3),(55,'2022-06-02 13:13:14.411970','9','Player object (9)',3,'',12,3),(56,'2022-06-02 13:13:14.417158','8','Player object (8)',3,'',12,3),(57,'2022-06-02 13:13:14.421953','7','Player object (7)',3,'',12,3),(58,'2022-06-02 13:13:14.426020','6','Player object (6)',3,'',12,3),(59,'2022-06-02 13:13:14.432269','5','Player object (5)',3,'',12,3),(60,'2022-06-02 13:13:14.436409','4','Player object (4)',3,'',12,3),(61,'2022-06-02 13:13:14.440365','3','Player object (3)',3,'',12,3),(62,'2022-06-02 13:13:20.705885','12','Team object (12)',3,'',11,3),(63,'2022-06-02 13:13:20.712002','11','Team object (11)',3,'',11,3),(64,'2022-06-02 13:13:20.716144','10','Team object (10)',3,'',11,3),(65,'2022-06-02 13:13:20.720021','9','Team object (9)',3,'',11,3),(66,'2022-06-02 13:13:20.723996','8','Team object (8)',3,'',11,3),(67,'2022-06-02 13:13:20.728421','7','Team object (7)',3,'',11,3),(68,'2022-06-02 13:13:20.732269','6','Team object (6)',3,'',11,3),(69,'2022-06-02 13:13:20.736270','5','Team object (5)',3,'',11,3),(70,'2022-06-02 13:13:20.740336','4','Team object (4)',3,'',11,3),(71,'2022-06-02 13:13:20.744625','3','Team object (3)',3,'',11,3),(72,'2022-06-02 13:13:29.830073','1','dp',3,'',6,3),(73,'2022-06-02 13:17:48.991030','7','berke',1,'[{\"added\": {}}]',6,3),(74,'2022-06-02 13:18:54.167910','7','berke',3,'',6,3),(75,'2022-06-02 13:20:17.934220','8','berke',1,'[{\"added\": {}}]',6,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 16:18:43
