from django.db import models

from .continent import Continent

class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    continentid = models.ForeignKey(Continent, models.DO_NOTHING, db_column='continentId')
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Countries'

    @staticmethod
    def get_country_from_iso2(iso2):
        return Country.objects.get(iso2=iso2)

    def __str__(self):
        return f"Country name: {self.name}, Iso2: {self.iso2}"
