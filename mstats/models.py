from django.db import models

# Create your models here.

class Info(models.Model):
    pid = models.BigIntegerField(max_length=20,primary_key=True)
    agent_id = models.IntegerField(max_length=11)
    server_id = models.IntegerField(max_length=11)
    mtime = models.IntegerField(max_length=11)
    stats = models.CharField(max_length=1000)
