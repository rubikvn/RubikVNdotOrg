from django.db import models

class Competition(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=50)
    cityname = models.CharField(db_column='cityName', max_length=50)
    countryid = models.CharField(db_column='countryId', max_length=50)
    information = models.TextField(blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField()
    day = models.PositiveSmallIntegerField()
    endmonth = models.PositiveSmallIntegerField(db_column='endMonth')
    endday = models.PositiveSmallIntegerField(db_column='endDay')
    eventspecs = models.CharField(db_column='eventSpecs', max_length=256, blank=True, null=True)
    wcadelegate = models.TextField(db_column='wcaDelegate', blank=True, null=True)
    organiser = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=240)
    venueaddress = models.CharField(db_column='venueAddress', max_length=120, blank=True, null=True)
    venuedetails = models.CharField(db_column='venueDetails', max_length=120, blank=True, null=True)
    external_website = models.CharField(max_length=200, blank=True, null=True)
    cellname = models.CharField(db_column='cellName', max_length=45)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Competitions'

    def __str__(self):
        return f"Competition name: {self.name}"


class Championship(models.Model):
    id = models.IntegerField(primary_key=True)
    competition_id = models.CharField(max_length=191)
    championship_type = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'championships'

    def __str__(self):
        return f"Championship name: {self.competition_id}"


class EligibleCountryIso2SForChampionship(models.Model):
    id = models.BigIntegerField(primary_key=True)
    championship_type = models.CharField(max_length=191)
    eligible_country_iso2 = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'eligible_country_iso2s_for_championship'

    def __str__(self):
        return f"ISO2S: {self.eligible_country_iso2}"
