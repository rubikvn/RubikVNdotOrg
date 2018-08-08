from django.db import models

class Rankaverage(models.Model):
    id = models.AutoField(primary_key=True)
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')  # Field name made lowercase.
    continentrank = models.IntegerField(db_column='continentRank')  # Field name made lowercase.
    countryrank = models.IntegerField(db_column='countryRank')  # Field name made lowercase.

    class Meta:
        db_table = 'RanksAverage'


class Ranksingle(models.Model):
    id = models.AutoField(primary_key=True)
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')  # Field name made lowercase.
    continentrank = models.IntegerField(db_column='continentRank')  # Field name made lowercase.
    countryrank = models.IntegerField(db_column='countryRank')  # Field name made lowercase.

    class Meta:
        db_table = 'RanksSingle'
