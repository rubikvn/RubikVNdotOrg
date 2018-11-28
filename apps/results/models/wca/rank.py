from django.db import models

from .person import Person
from .event import Event
from .competition import Competition

class RankAverage(models.Model):
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personId')
    eventid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eventId')
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')
    competitionid = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competitionId')

    class Meta:
        managed = False
        db_table = 'RanksAverage'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (average), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"

    @staticmethod
    def get_rank_average(eventid='333', limit='100', query=''):
        try:
            if limit == 'all':
                limit = None
            else:
                limit = int(limit)
            results = RankAverage.objects.values(
                'personid',
                'personid__name',
                'best',
                'countryrank',
                'competitionid',
                'competitionid__name'
            ).filter(
                eventid = eventid,
                personid__name__icontains = query
            ).order_by('best')[:limit]
            return results
        except ValueError:
            return []


class RankSingle(models.Model):
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personId')
    eventid = models.ForeignKey(Event, models.DO_NOTHING, db_column='eventId')
    best = models.IntegerField()
    worldrank = models.IntegerField(db_column='worldRank')
    continentrank = models.IntegerField(db_column='continentRank')
    countryrank = models.IntegerField(db_column='countryRank')
    competitionid = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competitionId')

    class Meta:
        managed = False
        db_table = 'RanksSingle'

    def __str__(self):
        return f"WCA ID: {self.personid}, event: {self.eventid} (single), result:{self.best} (WR{self.worldrank}, CR{self.continentrank}, NR{self.countryrank})"

    @staticmethod
    def get_rank_single(eventid='333', limit='100', query=''):
        try:
            if limit == 'all':
                limit = None
            else:
                limit = int(limit)
            results = RankSingle.objects.values(
                'personid',
                'personid__name',
                'best',
                'countryrank',
                'competitionid',
                'competitionid__name'
            ).filter(
                eventid = eventid,
                personid__name__icontains = query
            ).order_by('best')[:limit]
            return results
        except ValueError:
            return []
