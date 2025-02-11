from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'networks', NetworkViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'questions', QuestionsViewSet)
router.register(r'options', OptionViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'histories', HistoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart-item', CartItemViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('courses/', CourseListAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course_detail'),
    path('categories/', CategoryListAPIView.as_view(), name='categories_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail')


]
