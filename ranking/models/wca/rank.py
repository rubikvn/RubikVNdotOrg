from django.db import models

class Rankaverage(models.Model):
    id = models.AutoField(primary_key=True)
    personid = models.CharField(db_column='personId', max_length=10)
    eventid = models.CharField(db_column='eventId', max_length=6)
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')

    class Meta:
        db_table = 'RanksAverage'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (average), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"

    @staticmethod
    def get_rank_average(event='333', top='100'):
        pass


class Ranksingle(models.Model):
    id = models.AutoField(primary_key=True)
    personid = models.CharField(db_column='personId', max_length=10)
    eventid = models.CharField(db_column='eventId', max_length=6)
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')

    class Meta:
        db_table = 'RanksSingle'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (single), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"
