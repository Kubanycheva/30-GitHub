from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'phone_number', 'profile_picture']


class UserProfileCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()
    teacher_avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['subjects', 'experience', 'experience', 'teacher_avg_rating']

    def get_experience(self, obj):
        if obj.experience == 1:
            return f'{obj.experience} year'
        return f'{obj.experience} years'

    def get_teacher_avg_rating(self, obj):
        return obj.get_teacher_avg_rating()


class StudentSimpleSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()

    class Meta:
        model = Student
        fields = ['user', 'role']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializer(serializers.ModelSerializer):
    avg_stars = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField()
    change_price = serializers.SerializerMethodField()
    count_lesson = serializers.SerializerMethodField()
    author = UserProfileCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'price', 'level', 'type_course', 'author', 'course_image',
                  'avg_stars', 'count_people', 'discount_price', 'count_lesson', 'change_price']

    def get_avg_stars(self, obj):
        return obj.get_avg_stars()

    def get_count_people(self, obj):
        return obj.get_count_people()

    def get_discount_price(self, obj):
        return obj.get_discount_price()

    def get_change_price(self, obj):
        return obj.get_change_price()

    def get_count_lesson(self, obj):
        return obj.get_count_lesson()


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_course = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_course']


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryCourseSerializer(many=True)
    author = UserProfileCourseSerializer(many=True)
    count_people = serializers.SerializerMethodField()
    updated_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    created_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category',  'price', 'level', 'type_course', 'author', 'course_image',
                  'count_people', 'created_at', 'updated_at', 'course_certificate']

    def get_count_people(self, obj):
        return obj.course_review.count()


class LessonListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'video', 'content', 'course']


class LessonDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = Lesson
        fields = ['video', 'content', 'course']


class AssignmentListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    students = StudentSimpleSerializer()

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'course', 'students']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    students = StudentSimpleSerializer()

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']


class ExamSerializer(serializers.ModelSerializer):
    course = CourseListSerializer

    class Meta:
        model = Exam
        fields = '__all__'


class ExamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ['id', 'title', 'end_time']


class ExamDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = Exam
        fields = ['title', 'course', 'end_time']


class QuestionsListSerializer(serializers.ModelSerializer):
    exam = ExamListSerializer()

    class Meta:
        model = Questions
        fields = ['exam', 'title', 'score']


class QuestionsTeacherSerializer(serializers.ModelSerializer):
    exam = ExamListSerializer

    class Meta:
        model = Questions
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    questions = QuestionsListSerializer()

    class Meta:
        model = Option
        fields = '__all__'


class OptionListSerializer(serializers.ModelSerializer):
    questions = QuestionsListSerializer()

    class Meta:
        model = Option
        fields = ['id', 'questions', 'variant', 'option_check']


class OptionDetailSerializer(serializers.ModelSerializer):
    questions = QuestionsListSerializer()

    class Meta:
        model = Option
        fields = ['id', 'questions', 'variant', 'option_check']


class OptionTeacherSerializer(serializers.ModelSerializer):
    questions = QuestionsListSerializer()

    class Meta:
        model = Option
        fields = ['id', 'questions', 'variant', 'option_check']


class CertificateSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    student = StudentSimpleSerializer()

    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class CertificateCourseSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    student = StudentSimpleSerializer()

    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class CertificateStudentSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    student = StudentSimpleSerializer()

    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class CertificateListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    student = StudentSimpleSerializer()

    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']


class CertificateDetailSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()
    student = StudentSimpleSerializer()

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
    date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = History
        fields = ['student', 'course', 'date']
        

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


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
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
