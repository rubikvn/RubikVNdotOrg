from django.db import models

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    competitionid = models.CharField(db_column='competitionId', max_length=32)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)  # Field name made lowercase.
    pos = models.SmallIntegerField()
    best = models.IntegerField()
    average = models.IntegerField()
    personname = models.CharField(db_column='personName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    personid = models.CharField(db_column='personId', max_length=10)  # Field name made lowercase.
    personcountryid = models.CharField(db_column='personCountryId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    formatid = models.CharField(db_column='formatId', max_length=1)  # Field name made lowercase.
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    regionalsinglerecord = models.CharField(db_column='regionalSingleRecord', max_length=3, blank=True, null=True)  # Field name made lowercase.
    regionalaveragerecord = models.CharField(db_column='regionalAverageRecord', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Results'


class Scramble(models.Model):
    scrambleid = models.PositiveIntegerField(db_column='scrambleId', primary_key=True)  # Field name made lowercase.
    competitionid = models.CharField(db_column='competitionId', max_length=32)  # Field name made lowercase.
    eventid = models.CharField(db_column='eventId', max_length=6)  # Field name made lowercase.
    roundtypeid = models.CharField(db_column='roundTypeId', max_length=1)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=3)  # Field name made lowercase.
    isextra = models.IntegerField(db_column='isExtra')  # Field name made lowercase.
    scramblenum = models.IntegerField(db_column='scrambleNum')  # Field name made lowercase.
    scramble = models.TextField()

    class Meta:
        db_table = 'Scrambles'
