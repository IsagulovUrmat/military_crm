from django.db import models
from accounts.models import Dossier

class Education(models.Model):


    # start_date = models.DateField()
    # end_date = models.DateField()
    schoolname = models.CharField(max_length=50)
    # major = models.CharField(max_length=50)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return self.schoolname


class Warcraft(models.Model):


    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='warcraft')
    military_area = models.CharField(max_length=20)

    def __str__(self):
        return self.military_area

