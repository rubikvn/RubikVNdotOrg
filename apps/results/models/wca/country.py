from django.db import models

class Country(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    continentid = models.CharField(db_column='continentId', max_length=50)
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Countries'

    def __str__(self):
        return f"Country name: {self.name}, Iso2: {self.iso2}"
