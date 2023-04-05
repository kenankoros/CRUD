from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=25, blank=False, null=True)
    email = models.EmailField()
    age = models.IntegerField()
    gender=models.CharField(max_length=30, blank=False, null=True)


def _str_(self):
    return self.name
