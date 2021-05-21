from .models import *
from rest_framework import serializers, status




class EducationSerializer(serializers.ModelSerializer):
    edu_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Education
        fields = ['edu_id', 'schoolname']


class WarcraftSerializer(serializers.ModelSerializer):
    war_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Warcraft
        fields = ['war_id', 'military_area']