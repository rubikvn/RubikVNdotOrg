/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Competitions` (
  `id` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `cityName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `countryId` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `information` mediumtext COLLATE utf8mb4_unicode_ci,
  `year` smallint(5) unsigned NOT NULL DEFAULT '0',
  `month` smallint(5) unsigned NOT NULL DEFAULT '0',
  `day` smallint(5) unsigned NOT NULL DEFAULT '0',
  `endMonth` smallint(5) unsigned NOT NULL DEFAULT '0',
  `endDay` smallint(5) unsigned NOT NULL DEFAULT '0',
  `eventSpecs` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `wcaDelegate` text COLLATE utf8mb4_unicode_ci,
  `organiser` text COLLATE utf8mb4_unicode_ci,
  `venue` varchar(240) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `venueAddress` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `venueDetails` varchar(120) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `external_website` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cellName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `latitude` int(11) DEFAULT NULL,
  `longitude` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Continents` (
  `id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `recordName` char(3) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `latitude` int(11) NOT NULL DEFAULT '0',
  `longitude` int(11) NOT NULL DEFAULT '0',
  `zoom` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Countries` (
  `id` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `continentId` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `iso2` char(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Events` (
  `id` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(54) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `rank` int(11) NOT NULL DEFAULT '0',
  `format` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `cellName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Formats` (
  `id` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `sort_by` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sort_by_second` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expected_solve_count` int(11) NOT NULL,
  `trim_fastest_n` int(11) NOT NULL,
  `trim_slowest_n` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Persons` (
  `id` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `subid` tinyint(6) NOT NULL DEFAULT '1',
  `name` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `countryId` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `gender` char(1) COLLATE utf8mb4_unicode_ci DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RanksAverage` (
  `personId` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `eventId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `best` int(11) NOT NULL DEFAULT '0',
  `worldRank` int(11) NOT NULL DEFAULT '0',
  `continentRank` int(11) NOT NULL DEFAULT '0',
  `countryRank` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RanksSingle` (
  `personId` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `eventId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `best` int(11) NOT NULL DEFAULT '0',
  `worldRank` int(11) NOT NULL DEFAULT '0',
  `continentRank` int(11) NOT NULL DEFAULT '0',
  `countryRank` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Results` (
  `competitionId` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `eventId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `roundTypeId` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `pos` smallint(6) NOT NULL DEFAULT '0',
  `best` int(11) NOT NULL DEFAULT '0',
  `average` int(11) NOT NULL DEFAULT '0',
  `personName` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `personId` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `personCountryId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `formatId` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `value1` int(11) NOT NULL DEFAULT '0',
  `value2` int(11) NOT NULL DEFAULT '0',
  `value3` int(11) NOT NULL DEFAULT '0',
  `value4` int(11) NOT NULL DEFAULT '0',
  `value5` int(11) NOT NULL DEFAULT '0',
  `regionalSingleRecord` char(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `regionalAverageRecord` char(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RoundTypes` (
  `id` char(1) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `rank` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `cellName` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `final` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rounds` (
  `sorry_message` varchar(172) CHARACTER SET utf8 NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Scrambles` (
  `scrambleId` int(10) unsigned NOT NULL DEFAULT '0',
  `competitionId` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `eventId` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `roundTypeId` char(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `groupId` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isExtra` tinyint(1) NOT NULL,
  `scrambleNum` int(11) NOT NULL,
  `scramble` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `championships` (
  `id` int(11) NOT NULL DEFAULT '0',
  `competition_id` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `championship_type` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eligible_country_iso2s_for_championship` (
  `id` bigint(20) NOT NULL DEFAULT '0',
  `championship_type` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL,
  `eligible_country_iso2` varchar(191) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
