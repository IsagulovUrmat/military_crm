from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import *
from django.utils import timezone
import datetime

class DocumentSerializer(serializers.ModelSerializer):
    check_date = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Document
        fields = ['id', 'title', 'text', 'file', 'date_created', 'date_expired', 'status', 'document_root', 'check_date', 'user']

    def get_check_date(self, obj):
        date_expired = obj.date_expired
        date_now = datetime.datetime.date(timezone.now())
        if date_now > date_expired:
            obj.status = 'dead'
            obj.save()

    def create(self, validated_data):
        user = validated_data.pop('user')
        group = user.groups.all()[0].name
        doc_root = validated_data['document_root']
        if group == 'general' and doc_root in ['public', 'private', 'secret']:
            document = Document.objects.create(**validated_data)
        elif group == 'president':
            document = Document.objects.create(**validated_data)
        else:
            raise ValidationError("You have no permission!")
        return document



