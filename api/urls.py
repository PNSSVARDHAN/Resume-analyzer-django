from django.urls import path
from .views import StudentsView,StudentView

urlpatterns = [
    path("students/",StudentsView),
    path("student/<int:pk>",StudentView),
]