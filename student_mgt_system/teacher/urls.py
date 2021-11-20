from django.urls import path
from teacher import views

urlpatterns = [
    # path('', views.home, name='teacher-teacher_home'),
    path('', views.TeacherData.as_view()),
]
