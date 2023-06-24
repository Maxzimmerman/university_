from django.urls import path
from university_app.views import LandingPage, \
    Teachers, Students, Courses, CourseDetail, \
    CourseDelete, CourseUpdateView, AddNewCourse, \
    DeleteCourse, AddTeacher, CourseApi

urlpatterns = [
    # start page
    path("", LandingPage.as_view(), name="landing_page"),

    # teacher urls
    path("teachesrs", Teachers.as_view(), name="teachers"),
    path("add-teacher", AddTeacher.as_view(), name="add-teacher"),

    # student urls
    path("students", Students.as_view(), name="students"),

    # course urls
    path("courses", Courses.as_view(), name="courses"),
    path("courses/delete-show/<slug:slug>", CourseDelete.as_view(), name="course-detail-delete"),
    path("courses/detail/<slug:slug>", CourseDetail.as_view(), name="course-detail-page"),
    path("edit-course/<slug:slug>", CourseUpdateView.as_view(), name="edit-course"),
    path("add-course/", AddNewCourse.as_view(), name="add-course"),
    path("delete-course/<slug:slug>", DeleteCourse.as_view(), name="delete-course"),
    path("course-api", CourseApi.as_view(), name="course-api")
]
