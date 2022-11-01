from django.urls import path
from job import views

urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs')
]