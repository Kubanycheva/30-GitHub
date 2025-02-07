from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')  # Исправлено: ViewSet вместо модели
router.register(r'network', NetworkViewSet, basename='networks')
router.register(r'teacher', TeacherViewSet, basename='teachers')
router.register(r'student', StudentViewSet, basename='students')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'lesson', LessonViewSet, basename='lessons')
router.register(r'assignment', AssignmentViewSet, basename='assignments')  # Исправлено: убран лишний слеш
router.register(r'exam', ExamViewSet, basename='exams')  # Исправлено: убран лишний слеш
router.register(r'option', OptionViewSet, basename='options')  # Исправлено: убран лишний слеш
router.register(r'certificate', CertificateViewSet, basename='certificates')  # Исправлено: убран лишний слеш
router.register(r'history', HistoryViewSet, basename='histories')  # Исправлено: убран лишний слеш
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')  # Исправлено: убран лишний слеш
router.register(r'favorite', FavoriteViewSet, basename='favorites')
router.register(r'country', CountryViewSet, basename='countries')

urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseListApiView.as_view(), name='course_list'),
    path('course_detail/', CourseRetrieveUpdateApiView.as_view(), name='course_detail'),
    path('order/', OrderListApiView.as_view(), name='order_list'),
    path('order_list/', OrderRetrieveUpdateAPIView.as_view(), name='order_detail')
]
