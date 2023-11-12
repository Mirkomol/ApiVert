from rest_framework import serializers
from .models import TextroVertAppData
from django import forms


class TextroVertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextroVertAppData
        fields = ['id', 'name', 'data', 'category']



