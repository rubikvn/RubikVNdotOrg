-- Creates the db
CREATE DATABASE IF NOT EXISTS rubikvn;

use rubikvn;

-- Temporarily disable foreign key check for faster execution
SET FOREIGN_KEY_CHECKS=0;

-- Creates tables in the db
-- Competitions
DROP TABLE IF EXISTS Competitions;
DROP TABLE IF EXISTS Continents;
DROP TABLE IF EXISTS Countries;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Formats;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Results;
DROP TABLE IF EXISTS RanksAverage;
DROP TABLE IF EXISTS RanksSingle;
DROP TABLE IF EXISTS RoundTypes;
DROP TABLE IF EXISTS Rounds;
DROP TABLE IF EXISTS Scrambles;
DROP TABLE IF EXISTS championships;
DROP TABLE IF EXISTS eligible_country_iso2s_for_championship;

CREATE TABLE IF NOT EXISTS Competitions AS
    SELECT  *
    FROM wca.Competitions;

ALTER TABLE Competitions
ADD PRIMARY KEY (`id`);

-- Continents
CREATE TABLE IF NOT EXISTS Continents AS
    SELECT *
    FROM wca.Continents;

ALTER TABLE Continents
ADD PRIMARY KEY (`id`);

-- Countries
CREATE TABLE IF NOT EXISTS Countries AS
    SELECT *
    FROM  wca.Countries;

ALTER TABLE Countries
ADD PRIMARY KEY (`id`);

-- Events
CREATE TABLE IF NOT EXISTS Events AS
    SELECT *
    FROM wca.Events;

ALTER TABLE Events
ADD PRIMARY KEY (`id`);

-- Formats
CREATE TABLE IF NOT EXISTS Formats AS
    SELECT *
    FROM wca.Formats;

ALTER TABLE Formats
ADD PRIMARY KEY (`id`);

/*
 * Since we may be using sensitive information in this table (i.e emails, date of birth), a better way for extracting info from the WCA export would be to create a new table from the database export, and then join with the existing table in the db so that only new competitors are added into this table.
 */

-- or maybe don't put sensitive info on wca related db at all? And we can use WCA.org api for other functions.
-- Persons
CREATE TABLE IF NOT EXISTS Persons AS
    SELECT *
    FROM wca.Persons
    WHERE countryId = 'Vietnam';

ALTER TABLE Persons
ADD PRIMARY KEY (`id`);

-- Results
CREATE TABLE IF NOT EXISTS Results AS
    SELECT *
    FROM wca.Results
    WHERE personCountryId = 'Vietnam';

ALTER TABLE Results
ADD `id` int(10) PRIMARY KEY AUTO_INCREMENT;

-- RoundTypes
CREATE TABLE IF NOT EXISTS RoundTypes AS
    SELECT *
    FROM wca.RoundTypes;

ALTER TABLE RoundTypes
ADD PRIMARY KEY (`id`);

-- Rounds
CREATE TABLE IF NOT EXISTS Rounds AS
    SELECT *
    FROM wca.Rounds;

ALTER TABLE Rounds
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

-- Scrambles
CREATE TABLE IF NOT EXISTS Scrambles
    LIKE wca.Scrambles; 

ALTER TABLE Scrambles
ADD PRIMARY KEY (`scrambleId`);

-- championships
CREATE TABLE IF NOT EXISTS championships AS
    SELECT *
    FROM wca.championships;

ALTER TABLE championships
ADD PRIMARY KEY (`id`);

-- eligible_country_iso2s_for_championship
CREATE TABLE IF NOT EXISTS eligible_country_iso2s_for_championship AS
    SELECT *
    FROM wca.eligible_country_iso2s_for_championship;

ALTER TABLE eligible_country_iso2s_for_championship
ADD PRIMARY KEY (`id`);

-- Add foreign keys
ALTER TABLE Competitions
ADD FOREIGN KEY (countryId) REFERENCES Countries(id);

ALTER TABLE Countries
ADD FOREIGN KEY (continentId) REFERENCES Continents(id);

ALTER TABLE Persons
ADD FOREIGN KEY (countryId) REFERENCES Countries(id);

ALTER TABLE Results
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id),
ADD FOREIGN KEY (eventId) REFERENCES Events(id),
ADD FOREIGN KEY (roundTypeId) REFERENCES RoundTypes(id),
ADD FOREIGN KEY (personId) REFERENCES Persons(id),
ADD FOREIGN KEY (personCountryId) REFERENCES Countries(id),
ADD FOREIGN KEY (formatId) REFERENCES Formats(id);

ALTER TABLE Scrambles
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id),
ADD FOREIGN KEY (eventId) REFERENCES Events(id),
ADD FOREIGN KEY (roundTypeId) REFERENCES RoundTypes(id);

-- RanksAverage
CREATE TABLE IF NOT EXISTS RanksAverage AS
SELECT  a.personId,
a.eventId,
a.best,
a.worldRank,
a.continentRank,
a.countryRank,
b.competitionId
FROM wca.RanksAverage a
INNER JOIN rubikvn.Results b
ON a.personId = b.personId
AND a.best = b.average
GROUP BY b.personId, b.average;

-- RanksSingle
CREATE TABLE IF NOT EXISTS RanksSingle AS
SELECT  a.personId,
a.eventId,
a.best,
a.worldRank,
a.continentRank,
a.countryRank,
b.competitionId
FROM wca.RanksSingle a
INNER JOIN rubikvn.Results b
ON a.personId = b.personId
AND a.best = b.best
GROUP BY b.personId, b.best;

ALTER TABLE RanksAverage
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE RanksSingle
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE RanksAverage
ADD FOREIGN KEY (personId) REFERENCES Persons(id),
ADD FOREIGN KEY (eventId) REFERENCES Events(id),
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id);

ALTER TABLE RanksSingle
ADD FOREIGN KEY (personId) REFERENCES Persons(id),
ADD FOREIGN KEY (eventId) REFERENCES Events(id),
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id);

-- Re-enable foreign key check before exit
SET FOREIGN_KEY_CHECKS=1;
