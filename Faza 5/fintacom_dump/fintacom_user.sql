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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `Tokens` int NOT NULL,
  `Gold` int NOT NULL,
  `Silver` int NOT NULL,
  `Bronze` int NOT NULL,
  `Appearances` int NOT NULL,
  `Rank` int NOT NULL,
  `Profile_picture` varchar(100) DEFAULT NULL,
  `Tokens_given` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'pbkdf2_sha256$320000$IQ1I6FpR89tFLUHQBGGwex$UFcprlbrMEGJwg+5Yi7odhDqGt46vIHuHdjw8DRD3Z4=','2022-06-02 13:18:46.159444',1,'ivan','','','',1,1,'2022-06-01 10:18:36.101730',0,0,0,0,0,0,NULL,0),(6,'pbkdf2_sha256$320000$rR28IoeM5O0nTfZPub59Vh$nFFhkvdxEp06nv4t9KK9hTK1ZZsqFWM7fkB9/vzJ2Aw=','2022-06-02 14:03:40.208525',0,'tasha','Tamara','Sekularac','',0,1,'2022-06-02 13:15:18.943551',0,0,0,0,0,0,'profile_pictures/tasha_br_1.jpg',0),(8,'pbkdf2_sha256$320000$rR28IoeM5O0nTfZPub59Vh$nFFhkvdxEp06nv4t9KK9hTK1ZZsqFWM7fkB9/vzJ2Aw=','2022-06-02 13:20:51.878861',0,'berke','Uros','Beric','bu@etf.rs',1,1,'2022-06-02 13:18:56.000000',0,0,0,0,0,0,'profile_pictures/retriever1_5ZGwXhv.jpg',0),(9,'pbkdf2_sha256$320000$mJOQn2hBoss1f65uXfGXCo$Qvi21y8Tr1z1hWdSTY5VrZomqVr3DE4Nk6dSm6gfw9U=','2022-06-02 14:01:05.122856',0,'dp','Pavle','Divovic','',0,1,'2022-06-02 13:22:35.577916',0,0,0,0,0,0,'profile_pictures/beli1.jpg',0),(10,'pbkdf2_sha256$320000$ETHJmbVwRCApZVfY2Mw9EJ$gq0+tm5XhZshOPVNhp+J/uv/10BAF4cvekn1XwBnQ1o=','2022-06-02 13:41:25.248551',0,'zodra','Drazen','Draskovic','',0,1,'2022-06-02 13:24:02.639574',0,0,0,0,0,0,'profile_pictures/kanarinac1.jpg',0),(11,'pbkdf2_sha256$320000$sl6p7FXvrgFTo5sbBBD9qu$m0GfSqTjV7PuYqqBYiXDs5EB0hbUqt6U37iZJuF5J8Y=','2022-06-02 13:25:14.885348',0,'kolja','Konstantin','Benovic','',0,1,'2022-06-02 13:25:14.621349',0,0,0,0,0,0,'profile_pictures/3-2-love-hearts-eyes-emoji-png.png',0),(12,'pbkdf2_sha256$320000$bsCkeZq8sUz04MxwQXADTQ$uexp3w/SLkcBR6TQc6qBMQzrv3N2veKl+Vr1KQF4c4o=','2022-06-02 13:25:58.525333',0,'lekr','Slavko','Krstic','',0,1,'2022-06-02 13:25:58.283636',0,0,0,0,0,0,'profile_pictures/papagaj.jpg',0),(13,'pbkdf2_sha256$320000$gemlf9iOnlHIP07HGDGMUs$PZW/A0mMI8u6q+gIodOV6851Xek9pQqVQ3pxWFJtYHI=','2022-06-02 13:54:25.414942',0,'ogriz','Mihajlo','Ogrizovic','',0,1,'2022-06-02 13:26:40.226162',0,0,0,0,0,0,'profile_pictures/tosa-removebg-preview.png',0),(14,'pbkdf2_sha256$320000$otmyG2Z7K7EB5lRaZQjjog$oCujcT2Z+HQDOk3vllLVhMJKbt431S/28fKuk/1eoFo=','2022-06-02 14:00:38.278878',0,'dr_bojic','Dragan','Bojic','',0,1,'2022-06-02 13:27:38.676633',0,0,0,0,0,0,'profile_pictures/icons8-aquarium-100.png',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
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
