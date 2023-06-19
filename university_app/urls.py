from django.urls import path
from university_app.views import LandingPage, Teachers, Students, Courses, CourseDetail, CourseDelete

urlpatterns = [
    path("", LandingPage.as_view(), name="landing_page"),
    path("teachesrs", Teachers.as_view(), name="teachers"),
    path("students", Students.as_view(), name="students"),
    path("courses", Courses.as_view(), name="courses"),
    path("courses/<slug:slug>", view=CourseDetail.as_view(), name="course-detail-page"),
]
