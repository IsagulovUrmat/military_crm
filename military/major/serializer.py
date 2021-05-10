from .models import *
from rest_framework import serializers, status




class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ['id', 'schoolname']


class WarcraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warcraft
        fields = ['id', 'military_area']