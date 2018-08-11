from django.db import models

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    competitionid = models.CharField(db_column='competitionId', max_length=32)
    eventid = models.CharField(db_column='eventId', max_length=6)
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)
    pos = models.SmallIntegerField()
    best = models.IntegerField()
    average = models.IntegerField()
    personname = models.CharField(db_column='personName', max_length=80, blank=True, null=True)
    personid = models.CharField(db_column='personId', max_length=10)
    personcountryid = models.CharField(db_column='personCountryId', max_length=50, blank=True, null=True)
    formatid = models.CharField(db_column='formatId', max_length=1)
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    regionalsinglerecord = models.CharField(db_column='regionalSingleRecord', max_length=3, blank=True, null=True)
    regionalaveragerecord = models.CharField(db_column='regionalAverageRecord', max_length=3, blank=True, null=True)

    class Meta:
        db_table = 'Results'

    def __str__(self):
        result = lambda x : 'DNS' if x == -2 else 'DNF' if x == -1 else 'n/a' if x == 0 else x
        return f"Result of {self.personname} ({self.personid}) at {self.competitionid}. Best: {result(self.best)}, average: {result(self.average)}"


class Scramble(models.Model):
    scrambleid = models.PositiveIntegerField(db_column='scrambleId', primary_key=True)
    competitionid = models.CharField(db_column='competitionId', max_length=32)
    eventid = models.CharField(db_column='eventId', max_length=6)
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)
    groupid = models.CharField(db_column='groupId', max_length=3)
    isextra = models.IntegerField(db_column='isExtra')
    scramblenum = models.IntegerField(db_column='scrambleNum')
    scramble = models.TextField()

    class Meta:
        db_table = 'Scrambles'

    def __str__(self):
        return f"{self.scramble}"
