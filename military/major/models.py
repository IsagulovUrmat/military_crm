from django.db import models


class Education(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()
    schoolname = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

