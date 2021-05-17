from .models import *
from rest_framework import serializers, status




class EducationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Education
        fields = ['id', 'schoolname']


class WarcraftSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Warcraft
        fields = ['id', 'military_area']