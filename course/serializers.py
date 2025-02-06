from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'subjects', 'experience']


class StudentListSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'role']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'type_course', 'course_certificate', 'course_image']


class CourseDetailSerializer(serializers.ModelSerializer):
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'authot', 'level', 'price',
                  'type_course', 'created_at', 'update_at', 'course_certificate', 'course_image', 'get_count_people']

    def get_count_people(self):
        return self.course_review.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'video', 'content', 'course']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'student']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'end_time']


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['title', 'title', 'score']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Option
        fields = ['questions', 'variant', 'option_check']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = ['course', 'user', 'text', 'stars']


class TeacherRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher', 'user', 'stars']
        
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['student', 'course', 'date']
        

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['student']
        
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'course']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['student']


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['favorite', 'course']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['student', 'cart_item', 'status', 'nam_on_the_mape']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['sudent', 'cart_item', 'status', 'man_on_the_map', 'card_number', 'expiration_date', 'cvv', 'created_date', 'country']