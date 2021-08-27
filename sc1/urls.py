from django.contrib import admin
from django.urls import path, include

from .views import ListJobsView

urlpatterns = [
    path('', ListJobsView.as_view(), name='home'),
]