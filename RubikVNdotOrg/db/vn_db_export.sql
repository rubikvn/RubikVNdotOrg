-- Creates the db
DROP DATABASE IF EXISTS rubikvn;
CREATE DATABASE rubikvn;

use rubikvn;

-- Creates tables in the db
-- Competitions
DROP TABLE IF EXISTS Competitions;

CREATE TABLE IF NOT EXISTS Competitions AS
    SELECT  *
    FROM wca.Competitions;


-- Continents
DROP TABLE IF EXISTS Continents;

CREATE TABLE IF NOT EXISTS Continents AS
    SELECT *
    FROM wca.Continents;


-- Countries
DROP TABLE IF EXISTS Countries;

CREATE TABLE IF NOT EXISTS Countries AS
    SELECT *
    FROM  wca.Countries;


-- Events
DROP TABLE IF EXISTS Events;

CREATE TABLE IF NOT EXISTS Events AS
    SELECT *
    FROM wca.Events;


-- Formats
DROP TABLE IF EXISTS Formats;

CREATE TABLE IF NOT EXISTS Formats AS
    SELECT *
    FROM wca.Formats;

/*
 * Since we may be using sensitive information in this table (i.e emails, date of birth), a better way for extracting info from the WCA export would be to create a new table from the database export, and then join with the existing table in the db so that only new competitors are added into this table.
 */

 -- or maybe don't put sensitive info on wca related db at all? And we can use WCA.org api for other functions.
 -- Persons
DROP TABLE IF EXISTS Persons;

CREATE TABLE IF NOT EXISTS Persons AS
    SELECT *
    FROM wca.Persons
    WHERE countryId = 'Vietnam';


-- RanksAverage
DROP TABLE IF EXISTS RanksAverage;

CREATE TABLE IF NOT EXISTS RanksAverage AS
    SELECT *
    FROM wca.RanksAverage RankAvg
    WHERE RankAvg.personId IN
      (SELECT `id`
      FROM Persons);


-- RanksSingle
DROP TABLE IF EXISTS RanksSingle;

CREATE TABLE IF NOT EXISTS RanksSingle AS
    SELECT *
    FROM wca.RanksSingle RankSin
    WHERE RankSin.personId IN
      (SELECT `id`
      FROM Persons);


-- Results
DROP TABLE IF EXISTS Results;

CREATE TABLE IF NOT EXISTS Results AS
    SELECT *
    FROM wca.Results
    WHERE personCountryId = 'Vietnam';


-- RoundTypes
DROP TABLE IF EXISTS RoundTypes;

CREATE TABLE IF NOT EXISTS RoundTypes AS
    SELECT *
    FROM wca.RoundTypes;


-- Rounds
DROP TABLE IF EXISTS Rounds;

CREATE TABLE IF NOT EXISTS Rounds AS
    SELECT *
    FROM wca.Rounds;


-- Scrambles
DROP TABLE IF EXISTS Scrambles;

CREATE TABLE IF NOT EXISTS Scrambles AS
    SELECT *
    FROM wca.Scrambles Scram
    WHERE Scram.competitionId IN
      (SELECT `id`
      FROM Competitions);


-- championships
DROP TABLE IF EXISTS championships;

CREATE TABLE IF NOT EXISTS championships AS
    SELECT *
    FROM wca.championships;


-- eligible_country_iso2s_for_championship
DROP TABLE IF EXISTS eligible_country_iso2s_for_championship;

CREATE TABLE IF NOT EXISTS eligible_country_iso2s_for_championship AS
    SELECT *
    FROM wca.eligible_country_iso2s_for_championship;


-- Add primary keys
ALTER TABLE eligible_country_iso2s_for_championship
ADD PRIMARY KEY (`id`);

ALTER TABLE Competitions
ADD PRIMARY KEY (`id`);

ALTER TABLE Continents
ADD PRIMARY KEY (`id`);

ALTER TABLE Countries
ADD PRIMARY KEY (`id`);

ALTER TABLE Events
ADD PRIMARY KEY (`id`);

ALTER TABLE Formats
ADD PRIMARY KEY (`id`);

ALTER TABLE Persons
ADD PRIMARY KEY (`id`);

ALTER TABLE RanksAverage
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE RanksSingle
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE Results
ADD `id` int(10) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE RoundTypes
ADD PRIMARY KEY (`id`);

ALTER TABLE Rounds
ADD `id` int(6) PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE Scrambles
ADD PRIMARY KEY (`scrambleId`);

ALTER TABLE championships
ADD PRIMARY KEY (`id`);

-- Add foreign keys
ALTER TABLE Competitions
ADD FOREIGN KEY (countryId) REFERENCES Countries(id) ON DELETE CASCADE;

ALTER TABLE Countries
ADD FOREIGN KEY (continentId) REFERENCES Continents(id) ON DELETE CASCADE;

ALTER TABLE Persons
ADD FOREIGN KEY (countryId) REFERENCES Countries(id) ON DELETE CASCADE;

ALTER TABLE RanksAverage
ADD FOREIGN KEY (personId) REFERENCES Persons(id) ON DELETE CASCADE,
ADD FOREIGN KEY (eventId) REFERENCES Events(id) ON DELETE CASCADE;

ALTER TABLE RanksSingle
ADD FOREIGN KEY (personId) REFERENCES Persons(id) ON DELETE CASCADE,
ADD FOREIGN KEY (eventId) REFERENCES Events(id) ON DELETE CASCADE;

ALTER TABLE Results
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id) ON DELETE CASCADE,
ADD FOREIGN KEY (eventId) REFERENCES Events(id) ON DELETE CASCADE,
ADD FOREIGN KEY (roundTypeId) REFERENCES RoundTypes(id) ON DELETE CASCADE,
ADD FOREIGN KEY (personId) REFERENCES Persons(id) ON DELETE CASCADE,
ADD FOREIGN KEY (personCountryId) REFERENCES Countries(id) ON DELETE CASCADE,
ADD FOREIGN KEY (formatId) REFERENCES Formats(id) ON DELETE CASCADE;

ALTER TABLE Scrambles
ADD FOREIGN KEY (competitionId) REFERENCES Competitions(id) ON DELETE CASCADE,
ADD FOREIGN KEY (eventId) REFERENCES Events(id) ON DELETE CASCADE,
ADD FOREIGN KEY (roundTypeId) REFERENCES RoundTypes(id) ON DELETE CASCADE;
