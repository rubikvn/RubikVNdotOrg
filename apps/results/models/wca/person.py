from django.db import models

from .country import Country

class Person(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    subid = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryId')
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Persons'

    def __str__(self):
        return f"{self.id}, {self.name} ({self.gender}) from {self.countryid}"
