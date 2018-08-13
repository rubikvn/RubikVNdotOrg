from django.db import models

class Format(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=50)
    sort_by = models.CharField(max_length=255)
    sort_by_second = models.CharField(max_length=255)
    expected_solve_count = models.IntegerField()
    trim_fastest_n = models.IntegerField()
    trim_slowest_n = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Formats'

    def __str__(self):
        return f"Format name: {self.name}"
