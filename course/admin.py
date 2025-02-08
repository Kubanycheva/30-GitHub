from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 1




admin.site.register(UserProfile)
admin.site.register(Network)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(CourseReview)
admin.site.register(TeacherRating)
admin.site.register(History)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(Country)
admin.site.register(Order)
