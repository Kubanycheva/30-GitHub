from rest_framework import serializers
from .models import *


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class Network(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class Teacher(serializers.ModelSerializer):

