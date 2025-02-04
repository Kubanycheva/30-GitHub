from rest_framework import viewsets, permissions, status, generics
from serializers import *
from .models import *

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer