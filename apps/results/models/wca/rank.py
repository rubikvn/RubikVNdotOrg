from django.db import models

from .person import Person
from .event import Event

class RankAverage(models.Model):
    personid = models.ForeignKey(Person, models.CASCADE, db_column='personId')
    eventid = models.ForeignKey(Event, models.CASCADE, db_column='eventId')
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')

    class Meta:
        managed = False
        db_table = 'RanksAverage'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (average), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"

    @staticmethod
    def get_rank_average(eventid='333', limit='100'):
        try:
            if limit == 'All':
                limit = None
            else:
                limit = int(limit)
            results = RankAverage.objects.values(
                'personid', 'personid__name', 'best', 'countryrank'
            ).filter(
                eventid = eventid
            ).order_by('best')[:limit]
            return results
        except ValueError:
            return []


class RankSingle(models.Model):
    personid = models.ForeignKey(Person, models.CASCADE, db_column='personId')
    eventid = models.ForeignKey(Event, models.CASCADE, db_column='eventId')
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')

    class Meta:
        managed = False
        db_table = 'RanksSingle'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (single), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"

    @staticmethod
    def get_rank_single(eventid='333', limit='100'):
        try:
            if limit == 'All':
                limit = None
            else:
                limit = int(limit)
            results = RankSingle.objects.values(
                'personid', 'personid__name', 'best', 'countryrank'
            ).filter(
                eventid = eventid
            ).order_by('best')[:limit]
            return results
        except ValueError:
            return []
