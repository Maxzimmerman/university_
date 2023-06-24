from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Teacher(TimeStampedModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return fr"{self.first_name} {self.last_name}"


class Student(TimeStampedModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    course = models.OneToOneField("Course", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return fr"{self.first_name} {self.last_name}"


class Course(TimeStampedModel):
    title = models.CharField(max_length=10)
    available_seats = models.IntegerField(default=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return fr"{self.title}"


class Test(TimeStampedModel):
    title = models.CharField(max_length=20)
