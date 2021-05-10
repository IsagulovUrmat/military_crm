from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import *
from django.utils import timezone
import datetime

class DocumentSerializer(serializers.ModelSerializer):
    check_date = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'text', 'file', 'date_created', 'date_expired', 'status', 'document_root', 'check_date']

    def get_check_date(self, obj):
        date_expired = obj.date_expired
        date_now = datetime.datetime.date(timezone.now())
        if date_now > date_expired:
            obj.status = 'dead'
            obj.save()




