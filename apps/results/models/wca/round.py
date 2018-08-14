from django.db import models

class RoundType(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    cellname = models.CharField(db_column='cellName', max_length=45)
    final = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'RoundTypes'

    def __str__(self):
        return f"Round type: {self.cellname}"

class Round(models.Model):
    sorry_message = models.CharField(max_length=172)

    class Meta:
        managed = False
        db_table = 'Rounds'

    def __str__(self):
        return f"Message: {self.sorry_message}"
