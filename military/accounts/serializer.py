from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import *
from.services import mailing
from major.serializer import *
from major.models import *

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'mark']



class DossierSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)
    schools = EducationSerializer(many=True)
    warcraft = WarcraftSerializer(many=True)

    class Meta:
        model = Dossier
        fields = ['id', 'full_name', 'date_birth', 'image', 'gender', 'user', 'cars', 'schools', 'warcraft']

    def create(self, validated_data):

        cars_data = validated_data.pop('cars')
        schools_data = validated_data.pop('schools')
        warcrafts_data = validated_data.pop('warcraft')
        dossier = Dossier.objects.create(**validated_data)
        for car in cars_data:
            Car.objects.create(dossier=dossier, **car)
        for school in schools_data:
            Education.objects.create(dossier=dossier, **school)
        for wc in warcrafts_data:
            Warcraft.objects.create(dossier=dossier, **wc)
        return dossier


class RegisterSerializer(serializers.ModelSerializer):

    check_password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=(
        ('common', 'common'),
        ('warrior', 'warrior')
    ), write_only=True)

    dossier = DossierSerializer()


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'check_password', 'user_type', 'dossier']

    def create(self, validated_data):

        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        user = User.objects.create(**validated_data)
        if password != check_password:
            raise ValidationError("Password don't match")
        user.set_password(password)
        if user_type == 'warrior':
            user.is_active = True
            group = Group.objects.get(name='sergeant')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        Dossier.objects.create(user=user)
        return user





