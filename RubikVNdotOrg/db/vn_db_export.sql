-- Creates the db
CREATE DATABASE IF NOT EXISTS rubikvn;

use rubikvn;

-- Creates tables in the db
DROP TABLE IF EXISTS rubikvn.Competitions;

CREATE TABLE IF NOT EXISTS rubikvn.Competitions AS
    SELECT  *
    FROM wca.Competitions
    WHERE countryId = 'Vietnam';

ALTER TABLE rubikvn.Competitions
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.Continents;

CREATE TABLE IF NOT EXISTS rubikvn.Continents AS
    SELECT *
    FROM wca.Continents;

ALTER TABLE rubikvn.Continents
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.Countries;

CREATE TABLE IF NOT EXISTS rubikvn.Countries AS
    SELECT *
    FROM  wca.Countries;

ALTER TABLE rubikvn.Countries
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.Events;

CREATE TABLE IF NOT EXISTS rubikvn.Events AS
    SELECT *
    FROM wca.Events;

ALTER TABLE rubikvn.Events
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.Formats;

CREATE TABLE IF NOT EXISTS rubikvn.Formats AS
    SELECT *
    FROM wca.Formats;

ALTER TABLE rubikvn.Formats
ADD PRIMARY KEY (`id`);

/*
 * Since we may be using sensitive information in this table (i.e emails, date of birth), a better way for extracting info from the WCA export would be to create a new table from the database export, and then join with the existing table in the db so that only new competitors are added into this table.
 */

 -- or maybe don't put sensitive info on wca related db at all? And we can use WCA.org api for other functions.
DROP TABLE IF EXISTS rubikvn.Persons;

CREATE TABLE IF NOT EXISTS rubikvn.Persons AS
    SELECT *
    FROM wca.Persons
    WHERE countryId = 'Vietnam';

ALTER TABLE rubikvn.Persons
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.RanksAverage;

CREATE TABLE IF NOT EXISTS rubikvn.RanksAverage AS
    SELECT *
    FROM wca.RanksAverage RankAvg
    WHERE RankAvg.personId IN
      (SELECT `id`
      FROM Persons);

ALTER TABLE rubikvn.RanksAverage
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

--
DROP TABLE IF EXISTS rubikvn.RanksSingle;

CREATE TABLE IF NOT EXISTS rubikvn.RanksSingle AS
    SELECT *
    FROM wca.RanksSingle RankSin
    WHERE RankSin.personId IN
      (SELECT `id`
      FROM Persons);

ALTER TABLE rubikvn.RanksSingle
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

--
DROP TABLE IF EXISTS rubikvn.Results;

CREATE TABLE IF NOT EXISTS rubikvn.Results AS
    SELECT *
    FROM wca.Results
    WHERE personCountryId = 'Vietnam';

ALTER TABLE rubikvn.Results
ADD `id` int(10) PRIMARY KEY AUTO_INCREMENT;

--
DROP TABLE IF EXISTS rubikvn.RoundTypes;

CREATE TABLE IF NOT EXISTS rubikvn.RoundTypes AS
    SELECT *
    FROM wca.RoundTypes;

ALTER TABLE rubikvn.RoundTypes
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.Rounds;

CREATE TABLE IF NOT EXISTS rubikvn.Rounds AS
    SELECT *
    FROM wca.Rounds;

ALTER TABLE rubikvn.Rounds
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

--
DROP TABLE IF EXISTS rubikvn.Scrambles;

CREATE TABLE IF NOT EXISTS rubikvn.Scrambles AS
    SELECT *
    FROM wca.Scrambles Scram
    WHERE Scram.competitionId IN
      (SELECT `id`
      FROM Competitions);

ALTER TABLE rubikvn.Scrambles
ADD PRIMARY KEY (`scrambleId`);

--
DROP TABLE IF EXISTS rubikvn.championships;

CREATE TABLE IF NOT EXISTS rubikvn.championships AS
    SELECT *
    FROM wca.championships;

ALTER TABLE rubikvn.championships
ADD PRIMARY KEY (`id`);

--
DROP TABLE IF EXISTS rubikvn.eligible_country_iso2s_for_championship;

CREATE TABLE IF NOT EXISTS rubikvn.eligible_country_iso2s_for_championship AS
    SELECT *
    FROM wca.eligible_country_iso2s_for_championship;

ALTER TABLE rubikvn.eligible_country_iso2s_for_championship
ADD PRIMARY KEY (`id`);
