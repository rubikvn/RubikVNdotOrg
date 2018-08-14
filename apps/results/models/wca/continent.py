from django.db import models

class Continent(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    recordname = models.CharField(db_column='recordName', max_length=3)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    zoom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Continents'

    def __str__(self):
        return f"Continent name: {self.name}"
