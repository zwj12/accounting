from django.db import models

# Create your models here.
from cash.models import CommonInfo


class Commany(CommonInfo):
    # Note that when unique is True,
    # you don’t need to specify db_index,
    # because unique implies the creation of an index.
    company = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'cash_company'

    def __str__(self):
        return self.company
