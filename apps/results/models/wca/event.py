from django.db import models

FORMAT_TIME = [
    '222', '333', '333bf', '333ft',
    '333oh', '444', '444bf', '555',
    '555bf', '666', '777', 'clock',
    'magic', 'minx', 'mmagic', 'pyram',
    'skewb', 'sq1'
]
FORMAT_MULTI = ['333mbf', '333mbo']
FORMAT_NUMBER = ['333fm']

class Event(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=54)
    rank = models.IntegerField()
    format = models.CharField(max_length=10)
    cellname = models.CharField(db_column='cellName', max_length=45)

    class Meta:
        managed = False
        db_table = 'Events'

    def __str__(self):
        return f"Event name: {self.name}, format: {self.format}"

    @staticmethod
    def get_event_name(eventid):
        try:
            event =  Event.objects.get(pk=eventid)
            return event.name
        except Event.DoesNotExist:
            return ""
