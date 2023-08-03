# job_portal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('jobs/', views.jobs, name='jobs'),
    path('post_job/', views.post_job, name='post_job'),
    path('post_job/', views.job_post_submit, name='job_post_submit'),
    
]
