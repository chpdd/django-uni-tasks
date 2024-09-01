from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('task/<int:task_number>', views.task, name="task"),
    path('jquery_test', views.jquery_test, name="jquery_test")
]
