from django.db import models
from django.contrib.auth.models import User

class Dosier(models.Model):

    full_name = models.CharField(max_length=50)
    date_birth = models.DateField(auto_now_add=True)
    image = models.ImageField()
    gender = models.CharField(choices=(
        ('Female', 'Female'),
        ('Male', 'Male')
    ), max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

