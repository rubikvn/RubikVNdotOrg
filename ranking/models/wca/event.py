from django.db import models

class Event(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=54)
    rank = models.IntegerField()
    format = models.CharField(max_length=10)
    cellname = models.CharField(db_column='cellName', max_length=45)

    class Meta:
        db_table = 'Events'

    def __str__(self):
        return f"Event name: {self.name}, format: {self.format}"
