from django.urls import path
from views import *
urlpatterns = [
    path('login/', views.login, name='login'),
    path('edit/', views.edit, name='edit'),
    path('weekly/', views.weekly, name='weekly'),
    path('feedback/', views.feedback, name='feedback'),
]
