from django.db import models
from django.contrib.auth.models import User

class Dossier(models.Model):

    full_name = models.CharField(max_length=50)
    date_birth = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True)
    gender = models.CharField(choices=(
        ('Female', 'Female'),
        ('Male', 'Male')
    ), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Car(models.Model):


    mark = models.CharField(max_length=20)
    # model
    # year
    # number
    # color
    # type
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='cars')

