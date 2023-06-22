from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from university_app.models import Teacher, Student, Course, Test
from django.views import View
from .forms import CourseForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class LandingPage(TemplateView):
    template_name = "university_app/landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        context["teachers"] = Teacher.objects.all()
        context["students"] = Student.objects.all()

        return context


class Teachers(ListView):
    model = Teacher
    template_name = "university_app/teachers.html"


class Students(ListView):
    model = Student
    template_name = "university_app/students.html"


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


class CourseDelete(View):

    def get(self, reqeust, slug):
        entry = Course.objects.get(slug=slug)

        context = {
            "course": entry,
        }

        return render(reqeust, "university_app/course-delete.html", context)


class CourseUpdateView(UpdateView):
    model = Course
    fields = ["title", "available_seats", "slug"]
    template_name_suffix = "_update_form"
    success_url = "/courses"


# class eqivalientToAbov(View):
#     # returns form od adjust entry
#     def get(self, request, slug):
#         entry = Course.objects.get(slug=slug)
#         context = {
#             "course": entry,
#         }
#         return render(request, "university_app/course_update_form.html", context)
#     # get the post request of htmx form
#     def post(self, request):
#         request_form = request.POST()
#         new_entry = Course.objects.create(request_form)
#         new_entry.save()
#
#         return HttpResponseRedirect("/edit-course")


class AddNewCourse(CreateView):
    model = Course
    fields = ["title", "available_seats", "slug"]
    success_url = "/courses"


class DeleteCourse(DeleteView):
    model = Course
    success_url = "/courses"
