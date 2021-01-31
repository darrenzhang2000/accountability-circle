from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.edit, name='edit'),
    path('', include('django.contrib.auth.urls')), 
    path('weekly/', views.weekly, name='weekly'),
    path('feedback/', views.feedback, name='feedback'),
]
