from django.urls import path
from apiapp import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
     
]
