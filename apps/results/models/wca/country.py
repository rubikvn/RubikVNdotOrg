from django.db import models

from .continent import Continent

class Country(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    continentid = models.ForeignKey(Continent, models.CASCADE, db_column='continentId')
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Countries'

    def __str__(self):
        return f"Country name: {self.name}, Iso2: {self.iso2}"
