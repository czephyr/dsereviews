from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("courses/<slug:slug>", views.CourseDetail.as_view(), name="course_detail"),
    path(
        "professors/<slug:slug>",
        views.ProfessorDetail.as_view(),
        name="professor_detail",
    ),
    path("shb", views.shihab, name="shb"),
]
