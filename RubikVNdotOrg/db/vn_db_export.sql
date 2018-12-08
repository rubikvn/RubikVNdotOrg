-- Creates the db
CREATE DATABASE IF NOT EXISTS rubikvn;

use rubikvn;

-- Temporarily disable foreign key check for faster execution
SET FOREIGN_KEY_CHECKS=0;

-- Clear all WCA tables in the db
TRUNCATE Competitions;
TRUNCATE Continents;
TRUNCATE Countries;
TRUNCATE Events;
TRUNCATE Formats;
TRUNCATE Persons;
TRUNCATE Results;
TRUNCATE RanksAverage;
TRUNCATE RanksSingle;
TRUNCATE RoundTypes;
TRUNCATE Rounds;
TRUNCATE Scrambles;
TRUNCATE championships;
TRUNCATE eligible_country_iso2s_for_championship;

-- Competitions
INSERT INTO Competitions
    SELECT  *
    FROM wca.Competitions;

-- Continents
INSERT INTO Continents
    SELECT *
    FROM wca.Continents;

-- Countries
INSERT INTO Countries
    SELECT *
    FROM  wca.Countries;

-- Events
INSERT INTO Events
    SELECT *
    FROM wca.Events;

-- Formats
INSERT INTO Formats
    SELECT *
    FROM wca.Formats;

-- Persons
INSERT INTO Persons
    SELECT *
    FROM wca.Persons
    WHERE countryId = 'Vietnam';

-- Results
INSERT INTO Results (
        competitionId,
        eventId,
        roundTypeId,
        pos,
        best,
        average,
        personName,
        personId,
        personCountryId,
        formatId,
        value1,
        value2,
        value3,
        value4,
        value5,
        regionalSingleRecord,
        regionalAverageRecord
    )
    SELECT *
    FROM wca.Results
    WHERE personCountryId = 'Vietnam';

-- RoundTypes
INSERT INTO RoundTypes
    SELECT *
    FROM wca.RoundTypes;

-- Rounds
INSERT INTO Rounds (
        sorry_message
    )
    SELECT *
    FROM wca.Rounds;

-- Scrambles
INSERT INTO Scrambles
    SELECT *
    FROM wca.Scrambles;

-- championships
INSERT INTO championships
    SELECT *
    FROM wca.championships;

-- eligible_country_iso2s_for_championship
INSERT INTO eligible_country_iso2s_for_championship
    SELECT *
    FROM wca.eligible_country_iso2s_for_championship;

-- RanksAverage
INSERT INTO RanksAverage (
        personId,
        eventId,
        best,
        worldRank,
        continentRank,
        countryRank,
        competitionId
    )
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
INSERT INTO RanksSingle (
        personId,
        eventId,
        best,
        worldRank,
        continentRank,
        countryRank,
        competitionId
    )
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

-- Re-enable foreign key check before exit
SET FOREIGN_KEY_CHECKS=1;
