from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from university_app.models import Teacher, Student, Course, Test
from django.views import View
from .forms import CourseForm
from django.http import HttpResponseRedirect, HttpResponse


# from rest_framework.views import APIView
# from rest_framework.response import Response

# Create your views here.

class LandingPage(TemplateView):
    template_name = "university_app/landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        context["teachers"] = Teacher.objects.all()
        context["students"] = Student.objects.all()

        return context


class Teachers(View):
    def get(self, request):
        entries = Teacher.objects.all()

        context = {
            "teachers": entries
        }

        return render(request, "university_app/teachers.html", context)


class AddTeacher(CreateView):
    model = Teacher
    fields = ["first_name", "last_name", "age", "course", "slug"]
    success_url = "http://localhost:8000/teachesrs"


class DetailTeacher(View):
    def get(self, request, slug):
        entry = Teacher.objects.get(slug=slug)

        context = {
            "teacher": entry
        }

        return render(request, "university_app/teacher-detail.html", context)


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ["first_name", "last_name", "age", "course", "slug"]
    success_url = "http://localhost:8000/teachesrs"


class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = "http://localhost:8000/teachesrs"


class Students(ListView):
    model = Student
    template_name = "university_app/students.html"


class DetailStudent(View):
    def get(self, request, slug):
        student = Student.objects.get(slug=slug)

        context = {
            "students": student,
        }

        return render(request, "university_app/student-detail.html", context)

class AddStudent(CreateView):
    model = Student
    fields = ["first_name", "last_name", "age", "course", "slug"]
    success_url = "http://localhost:8000/students"

class RemoveStudent(View):
    def get(self, request, slug):
        student = Student.objects.get(slug=slug)

        context = {
            "student": student
        }

        return render(request, "", context)


class DeleteStudent(DeleteView):
    model = Student
    success_url = "http://localhost:8000/students"

class Courses(ListView):
    model = Course
    template_name = "university_app/courses.html"


class CourseDetail(View):

    def get(self, request, slug):
        # get entry of database
        course = Course.objects.get(slug=slug)

        # make the entry available
        context = {
            "course": course,
        }

        # rendering the view
        return render(request, "university_app/course-detail.html", context)


class AddNewCourse(CreateView):
    model = Course
    fields = ["title", "available_seats", "slug"]
    success_url = "/courses"


class CourseUpdateView(UpdateView):
    model = Course
    fields = ["title", "available_seats", "slug"]
    template_name_suffix = "_update_form"
    success_url = "/courses"


class CourseDelete(View):

    def get(self, reqeust, slug):
        entry = Course.objects.get(slug=slug)

        context = {
            "course": entry,
        }

        return render(reqeust, "university_app/course-delete.html", context)


class DeleteCourse(DeleteView):
    model = Course
    success_url = "/courses"


class CourseApi(View):
    def get(self, request):
        courses = Course.objects.all()
        return HttpResponse(courses)
