from django.urls import path,  include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfile, basename='users')
router.register(r'network', NetworkViewSet, basename='networks')

urlpatterns = [
    path('', include(router.urls)),

    path('course/', CourseListApiView)

]