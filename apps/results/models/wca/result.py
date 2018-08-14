from django.db import models

from .competition import Competition
from .country import Country
from .event import Event
from .format import Format
from .person import Person
from .round import RoundType

class Result(models.Model):
    competitionid = models.ForeignKey(Competition, models.CASCADE, db_column='competitionId')
    eventid = models.ForeignKey(Event, models.CASCADE, db_column='eventId')
    roundtypeid = models.ForeignKey(RoundType, models.CASCADE, db_column='roundTypeId')
    pos = models.SmallIntegerField()
    best = models.IntegerField()
    average = models.IntegerField()
    personname = models.CharField(db_column='personName', max_length=80, blank=True, null=True)
    personid = models.ForeignKey(Person, models.CASCADE, db_column='personId')
    personcountryid = models.ForeignKey(Country, models.CASCADE, db_column='personCountryId', blank=True, null=True)
    formatid = models.ForeignKey(Format, models.CASCADE, db_column='formatId')
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    regionalsinglerecord = models.CharField(db_column='regionalSingleRecord', max_length=3, blank=True, null=True)
    regionalaveragerecord = models.CharField(db_column='regionalAverageRecord', max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Results'

    def __str__(self):
        result = lambda x : 'DNS' if x == -2 else 'DNF' if x == -1 else 'n/a' if x == 0 else x
        return f"Result of {self.personname} ({self.personid}) at {self.competitionid}. Best: {result(self.best)}, average: {result(self.average)}"


class Scramble(models.Model):
    scrambleid = models.PositiveIntegerField(db_column='scrambleId', primary_key=True)
    competitionid = models.ForeignKey(Competition, models.CASCADE, db_column='competitionId')
    eventid = models.ForeignKey(Event, models.CASCADE, db_column='eventId')
    roundtypeid = models.ForeignKey(RoundType, models.CASCADE, db_column='roundTypeId')
    groupid = models.CharField(db_column='groupId', max_length=3)
    isextra = models.IntegerField(db_column='isExtra')
    scramblenum = models.IntegerField(db_column='scrambleNum')
    scramble = models.TextField()

    class Meta:
        managed = False
        db_table = 'Scrambles'

    def __str__(self):
        return f"{self.scramble}"
