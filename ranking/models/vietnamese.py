from django.db import models

class Vietnamese(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    subid = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.CharField(db_column='countryId', max_length=50)
    gender = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField()
    email = models.CharField(max_length=320)

    class Meta:
        db_table = 'Vietnamese'

    def __str__(self):
        return f"{self.id} - {self.name}, {self.gender}"
