from django.urls import path, include
from . import views
urlpatterns = [
    path('settings/', views.edit, name='edit'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('weekly/', views.weekly, name='weekly'),
    path('displaymissions/', views.displayMissions, name='displaymissions'),
    path('feedback/', views.feedback, name='feedback'),
    path('match/', views.match, name='match'),
]
