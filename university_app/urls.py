from django.urls import path
from university_app.views import LandingPage, \
    Teachers, Students, Courses, CourseDetail, \
    CourseDelete, CourseUpdateView, AddNewCourse, DeleteCourse

urlpatterns = [
    path("", LandingPage.as_view(), name="landing_page"),
    path("teachesrs", Teachers.as_view(), name="teachers"),
    path("students", Students.as_view(), name="students"),
    path("courses", Courses.as_view(), name="courses"),
    path("courses/delete-show/<slug:slug>", CourseDelete.as_view(), name="course-detail-delete"),
    path("courses/detail/<slug:slug>", CourseDetail.as_view(), name="course-detail-page"),
    path("edit-course/<slug:slug>", CourseUpdateView.as_view(), name="edit-course"),
    path("add-course/", AddNewCourse.as_view(), name="add-course"),
    path("delete-course/<slug:slug>", DeleteCourse.as_view(), name="delete-course")
]
