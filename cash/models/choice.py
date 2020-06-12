from django.db import models


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    serial_number = models.IntegerField("sequence", default=1)
    lucre = models.FloatField()
    balance = models.FloatField(editable=False)
    # balance = models.FloatField()
