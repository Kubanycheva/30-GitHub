from h11 import Response
from rest_framework import viewsets, permissions, status, generics
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter
# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country_name']


class CourseDetailAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDetailApiView(generics.RetrieveUpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class AssignmentListApiView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer


class AssignmentDetailApiView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
     =


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        cart, created = Favorite.objects.get_or_create(user=self.request.user)
        serializer = self.get_serializer(cart)
        return Response(serializers.data)


class FavoriteItemViewSet(viewsets.ModelViewSet):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializer

    def get_queryset(self):
        return FavoriteItem.objects.filter(favorite__user__user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Favorite.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CourseListSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


