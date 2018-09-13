from django.db import models


class Cache(models.Model):
    text = models.CharField(max_length=256)
    content = models.TextField()
    dimension = models.CharField(max_length=100)
    status = models.IntegerField()
