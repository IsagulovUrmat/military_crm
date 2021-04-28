from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import *

class Dosier(serializers.ModelSerializer):

    class Meta:
        model = Dosier
        fields = '__all__'
