from django.db import models


class CommonInfo(models.Model):
    remark = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        abstract = True
