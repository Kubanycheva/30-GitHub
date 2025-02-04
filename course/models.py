from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

ROLE_CHOICES = (
    ('teacher', 'teacher'),
    ('student', 'student')
)

STATUS_CHOICES = (
    ('легкий', 'легкий'),
    ('средний', 'средний'),
    ('сложный', 'сложный')
)


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(15),
                                                       MaxValueValidator(60)],
                                           null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def str(self):
        return f'{self.first_name}, {self.last_name}'


class Network(models.Model):
    network_name = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.network_name}'