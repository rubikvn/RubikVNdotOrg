from django.db import models

class Person(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    subid = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.CharField(db_column='countryId', max_length=50)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Persons'

    def __str__(self):
        return f"{self.id}, {self.name} ({self.gender}) from {self.countryid}"
