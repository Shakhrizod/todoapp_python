from django.db import models


# Create your models here.
class Main(models.Model):
    added_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=200)