from django.db import models

class Country(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    continentid = models.CharField(db_column='continentId', max_length=50)  # Field name made lowercase.
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'Countries'
