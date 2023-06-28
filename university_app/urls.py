from django.urls import path
from university_app.views import LandingPage, \
    Teachers, Students, Courses, CourseDetail, \
    CourseDelete, CourseUpdateView, AddNewCourse, \
    DeleteCourse, AddTeacher, CourseApi, DetailTeacher, \
    UpdateTeacher, DeleteTeacher, DetailStudent, AddStudent, \
    RemoveStudent, DeleteStudent

urlpatterns = [
    # start page
    path("", LandingPage.as_view(), name="landing_page"),

    # teacher urls
    path("teachesrs", Teachers.as_view(), name="teachers"),
    path("add-teacher", AddTeacher.as_view(), name="add-teacher"),
    path("teacher-detail<slug:slug>", DetailTeacher.as_view(), name="detail-teacher"),
    path("teacher-edit<slug:slug>", UpdateTeacher.as_view(), name="update-teacher"),
    path("delete-teacher/<slug:slug>", DeleteTeacher.as_view(), name="delete-teacher"),

    # student urls
    path("students", Students.as_view(), name="students"),
    path("students/student-detail/<slug:slug>", DetailStudent.as_view(), name="student-detail"),
    path("student-add", AddStudent.as_view(), name="add-new-student"),
    path("students/student-delete/<slug:slug>", RemoveStudent.as_view(), name="remove-student"),
    path("students/delete-student/<slug:slug>", DeleteStudent.as_view(), name='delete-student'),

    # course urls
    path("courses", Courses.as_view(), name="courses"),
    path("courses/delete-show/<slug:slug>", CourseDelete.as_view(), name="course-detail-delete"),
    path("courses/detail/<slug:slug>", CourseDetail.as_view(), name="course-detail-page"),
    path("edit-course/<slug:slug>", CourseUpdateView.as_view(), name="edit-course"),
    path("add-course/", AddNewCourse.as_view(), name="add-course"),
    path("delete-course/<slug:slug>", DeleteCourse.as_view(), name="delete-course"),
    path("course-api", CourseApi.as_view(), name="course-api")
]
