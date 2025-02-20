from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart-item', CartItemViewSet, basename='cart_list')
router.register(r'cart', CartViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('courses/', CourseListAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),

    path('categories/', CategoryListAPIView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),

    path('lessons/', LessonListApiView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonDetailApiView.as_view(), name='lessons_list'),

    path('assignments/', AssignmentListApiView.as_view(), name='assignment_list'),
    path('assignments/<int:pk>/', AssignmentDetailApiView.as_view(), name='assignment_detail'),

    path('exams/', ExamListApiView.as_view(), name='exam_list'),
    path('exams/<int:pk>/', ExamDetailApiView.as_view(), name='exam_detail'),
    path('exam_teacher/', ExamTeacherListApiView.as_view(), name='exam_teacher_list'),
    path('exam_create/', ExamTeacherCreateApiView.as_view(), name='exam_create'),

    path('questions/', QuestionsListApiView.as_view(), name='questions_list'),
    path('questions_create/', QuestionsTeacherCreateApiView.as_view(), name='questions_list_create'),

    path('option_list/', OptionListApiView.as_view(), name='options_list'),
    path('option_list/<int:pk>/', OptionRetrieveUpdateAPIView.as_view(), name='options_detail'),
    path('option_create/<int:pk>', OptionRetrieveDestroyAPIView.as_view(), name='options_delete'),
    path('option_create/', OptionListCreateAPIView.as_view(), name='options_create'),

    path('certificate_list/', CertificateListCreateAPIView.as_view(), name='certificate_list'),
    path('certificate_list/<int:pk>/', CertificateRetrieveDestroyAPIView.as_view(), name='certificate_detail'),
    path('certificate_student/', CertificateListAPIView.as_view(), name='certificate_student'),
    path('certificate_student/<int:pk>/', CertificateRetrieveUpdateAPIView.as_view(), name='certificate_detail'),





]
