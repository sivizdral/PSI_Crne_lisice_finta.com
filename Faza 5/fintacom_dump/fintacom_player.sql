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
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `idPlayer` int NOT NULL AUTO_INCREMENT,
  `Forename` varchar(255) NOT NULL,
  `Surname` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Country` varchar(255) NOT NULL,
  `Position` varchar(255) NOT NULL,
  `idTeam` int NOT NULL,
  `Age` int NOT NULL,
  `Photo` varchar(255) NOT NULL,
  `Id` int NOT NULL,
  `Offence` int NOT NULL DEFAULT '0',
  `Defence` int NOT NULL DEFAULT '0',
  `Overall` int NOT NULL DEFAULT '0',
  `Value` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`idPlayer`),
  KEY `player_idTeam_b69c1ebb_fk_team_idTeam` (`idTeam`),
  CONSTRAINT `player_idTeam_b69c1ebb_fk_team_idTeam` FOREIGN KEY (`idTeam`) REFERENCES `team` (`idTeam`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (14,'Robert','Lewandowski','Robert Lewandowski','Poland','GK',1,34,'https://media.api-sports.io/football/players/521.png',521,0,1,-1,295),(15,'Serge David','Gnabry','Serge David Gnabry','Germany','LWB',2,27,'https://media.api-sports.io/football/players/510.png',510,0,57,57,219),(16,'Leroy Aziz','Sané','Leroy Aziz Sané','Germany','LCB',3,26,'https://media.api-sports.io/football/players/644.png',644,0,36,33,198),(17,'Manuel Peter','Neuer','M. Neuer','Germany','RCB',4,36,'https://media.api-sports.io/football/players/497.png',497,0,16,16,251),(18,'Thomas','Müller','Thomas Müller','Germany','RWB',5,33,'https://media.api-sports.io/football/players/522.png',522,0,43,43,257),(19,'Corentin','Tolisso','Corentin Tolisso','France','LM',6,28,'https://media.api-sports.io/football/players/519.png',519,1,18,19,70),(20,'Kingsley Junior','Coman','Kingsley Junior Coman','France','CM',7,26,'https://media.api-sports.io/football/players/508.png',508,2,20,19,136),(21,'Joshua Walter','Kimmich','Joshua Walter Kimmich','Germany','RM',8,27,'https://media.api-sports.io/football/players/502.png',502,8,78,82,247),(22,'Leon Christoph','Goretzka','Leon Christoph Goretzka','Germany','LAM',9,27,'https://media.api-sports.io/football/players/511.png',511,15,0,15,140),(23,'Marcel','Sabitzer','Marcel Sabitzer','Austria','RAM',10,28,'https://media.api-sports.io/football/players/1159.png',1159,8,0,8,89),(24,'Manuel Paul','Wintzheimer','Manuel Paul Wintzheimer','Germany','SS',11,23,'https://media.api-sports.io/football/players/24890.png',24890,13,0,10,59),(25,'Kylian','Mbappé Lottin','Kylian Mbappé Lottin','France','GK',12,24,'https://media.api-sports.io/football/players/278.png',278,0,1,-9,303),(26,'Neymar','da Silva Santos Júnior','Neymar da Silva Santos Júnior','Brazil','LWB',13,30,'https://media.api-sports.io/football/players/276.png',276,0,38,28,186),(27,'Lionel Andrés','Messi Cuccittini','L. Messi','Argentina','LCB',14,35,'https://media.api-sports.io/football/players/154.png',154,0,21,21,215),(28,'Achraf','Hakimi Mouh','Achraf Hakimi Mouh','Spain','RCB',15,24,'https://media.api-sports.io/football/players/9.png',9,0,85,80,248),(29,'Marcos','Aoás Corrêa','Marcos  Aoás Corrêa','Brazil','RWB',16,28,'https://media.api-sports.io/football/players/257.png',257,0,48,43,286),(30,'Gianluigi','Donnarumma','Gianluigi Donnarumma','Italy','LM',17,23,'https://media.api-sports.io/football/players/1622.png',1622,1,1,1,10),(31,'Nuno Alexandre','Tavares Mendes','Nuno Mendes','Portugal','CM',18,20,'https://media.api-sports.io/football/players/263482.png',263482,1,32,30,165),(32,'Leandro Daniel','Paredes','Leandro Daniel Paredes','Argentina','RM',19,28,'https://media.api-sports.io/football/players/271.png',271,0,31,28,84),(33,'Ousmane','Dembélé','Ousmane Dembélé','France','LAM',20,25,'https://media.api-sports.io/football/players/153.png',153,15,0,12,141),(34,'David','de Gea Quintana','David de Gea Quintana','Spain','GK',21,32,'https://media.api-sports.io/football/players/882.png',882,0,96,96,342),(35,'Marcelo','Vieira da Silva Júnior','Marcelo Vieira da Silva Júnior','Brazil','LWB',22,34,'https://media.api-sports.io/football/players/743.png',743,0,21,21,52),(36,'Mats','Hummels','Mats  Hummels','Germany','LCB',23,34,'https://media.api-sports.io/football/players/501.png',501,0,44,40,176),(37,'Thiago Emiliano','da Silva','Thiago Emiliano da Silva','Brazil','RCB',24,38,'https://media.api-sports.io/football/players/259.png',259,0,43,41,264),(38,'Karim','Benzema','K. Benzema','France','SS',25,35,'https://media.api-sports.io/football/players/759.png',759,99,0,99,260),(39,'Kevin','De Bruyne','Kevin De Bruyne','Belgium','RM',26,31,'https://media.api-sports.io/football/players/629.png',629,8,45,51,220),(40,'Aleksandar','Katai','Aleksandar Katai','Serbia','RAM',27,31,'https://media.api-sports.io/football/players/50910.png',50910,73,1,1,10),(41,'Aleksandar','Dragović','Aleksandar Dragović','Austria','RWB',28,31,'https://media.api-sports.io/football/players/968.png',968,1,1,1,10),(42,'Martin','Ødegaard','Martin Ødegaard','Norway','CM',29,24,'https://media.api-sports.io/football/players/37127.png',37127,7,51,54,279),(43,'Milan','Borjan','Milan Borjan','Croatia','GK',30,35,'https://media.api-sports.io/football/players/336.png',336,0,1,-1,270),(44,'Trent','Alexander-Arnold','Trent Alexander-Arnold','England','LWB',31,24,'https://media.api-sports.io/football/players/283.png',283,0,49,47,285),(45,'Ibrahima','Konaté','Ibrahima Konaté','France','LCB',32,23,'https://media.api-sports.io/football/players/1145.png',1145,0,28,26,99),(46,'Virgil','van Dijk','Virgil van Dijk','Netherlands','RCB',33,31,'https://media.api-sports.io/football/players/290.png',290,0,30,27,306),(47,'Konstantinos','Tsimikas','Konstantinos Tsimikas','Greece','RWB',34,26,'https://media.api-sports.io/football/players/1600.png',1600,0,37,34,87),(48,'Mohamed','Salah Ghaly','Mohamed Salah Ghaly','Egypt','SS',35,30,'https://media.api-sports.io/football/players/306.png',306,87,0,86,276),(49,'Takumi','Minamino','Takumi Minamino','Japan','RAM',36,27,'https://media.api-sports.io/football/players/1101.png',1101,10,1,1,10),(50,'Loris','Karius','Loris Karius','Germany','LAM',37,29,'https://media.api-sports.io/football/players/1972.png',1972,1,1,1,10),(51,'Harvey','Elliott','H. Elliott','England','RM',38,19,'https://media.api-sports.io/football/players/19035.png',19035,0,8,8,34),(52,'Thiago','Alcântara do Nascimento','Thiago Alcântara do Nascimento','Italy','CM',39,31,'https://media.api-sports.io/football/players/507.png',507,2,49,49,153),(53,'Sadio','Mané','Sadio Mané','Senegal','LM',40,30,'https://media.api-sports.io/football/players/304.png',304,4,34,33,282),(55,'Olivier','Giroud','Olivier Giroud','France','SS',42,36,'https://media.api-sports.io/football/players/2295.png',2295,41,0,37,190),(56,'Zlatan','Ibrahimović','Z. Ibrahimović','Sweden','RAM',43,41,'https://media.api-sports.io/football/players/51070.png',51070,31,0,29,100),(57,'Rafael Alexandre','da Conceição Leão','Rafael Alexandre da Conceição Leão','Portugal','LAM',44,23,'https://media.api-sports.io/football/players/22236.png',22236,46,0,42,262),(58,'Marko','Lazetić','M. Lazetić','Serbia','RM',45,18,'https://media.api-sports.io/football/players/162045.png',162045,1,1,1,10),(59,'Franck Yannick','Kessié','Franck Yannick Kessié','Côte d\'Ivoire','CM',46,26,'https://media.api-sports.io/football/players/1642.png',1642,2,43,43,230),(60,'Sandro','Tonali','S. Tonali','Italy','LM',47,22,'https://media.api-sports.io/football/players/31146.png',31146,4,45,40,260),(61,'Fikayo','Tomori','Fikayo Tomori','Canada','RWB',48,25,'https://media.api-sports.io/football/players/19209.png',19209,0,85,81,271),(62,'Theo Bernard François','Hernández','Theo Bernard François Hernández','France','RCB',49,25,'https://media.api-sports.io/football/players/47300.png',47300,0,65,57,271),(63,'Junior Walter','Messias','Junior Walter Messias','Brazil','LCB',50,31,'https://media.api-sports.io/football/players/56396.png',56396,0,43,41,142),(64,'Erling','Braut Håland','Erling Braut Håland','England','LWB',51,22,'https://media.api-sports.io/football/players/1100.png',1100,0,11,8,191),(65,'Lionel Andrés','Messi Cuccittini','L. Messi','Argentina','GK',52,35,'https://media.api-sports.io/football/players/154.png',154,0,1,1,215),(67,'Milan','Pavkov','Milan Pavkov','Serbia','RAM',54,28,'https://media.api-sports.io/football/players/365.png',365,34,1,1,10),(68,'Cristiano Ronaldo','dos Santos Aveiro','Cristiano Ronaldo','Portugal','SS',55,37,'https://media.api-sports.io/football/players/874.png',874,62,0,54,245);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
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
