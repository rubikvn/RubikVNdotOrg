from django.db import models

class Person(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    subid = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.CharField(db_column='countryId', max_length=50)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'Persons'