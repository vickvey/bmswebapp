from django.db import models
from django.conf import settings


ACC_NUM_LEN=settings.DATA['ACC_NUM_LEN']


class Account(models.Model):
    name=models.CharField(max_length=100)
    account_number=models.CharField(max_length=ACC_NUM_LEN)
    balance=models.FloatField()
    
    def __str__(self):
        return self.name