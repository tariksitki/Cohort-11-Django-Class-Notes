
from django.urls import path

from .views import index, student_add, student_delete, student_detail, student_list, student_update

urlpatterns = [
    path("", index, name="index"),
    path("list/", student_list, name="student_list"),
    path("add/", student_add, name="student_add"),
    path("update/<int:id>/", student_update, name="student_update"),
    path("delete/<int:id>/", student_delete, name="student_delete"),
    path('student/<int:id>/', student_detail, name="detail"),
]