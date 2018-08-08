from django.db import models

class Continent(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    recordname = models.CharField(db_column='recordName', max_length=3)  # Field name made lowercase.
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    zoom = models.IntegerField()

    class Meta:
        db_table = 'Continents'
