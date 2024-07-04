from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=35)
    body=models.CharField(max_length=5000)
