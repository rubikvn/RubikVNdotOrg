from django.db import models

class Roundtype(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    cellname = models.CharField(db_column='cellName', max_length=45)  # Field name made lowercase.
    final = models.IntegerField()

    class Meta:
        db_table = 'RoundTypes'


class Round(models.Model):
    id = models.AutoField(primary_key=True)
    sorry_message = models.CharField(max_length=172)

    class Meta:
        db_table = 'Rounds'
