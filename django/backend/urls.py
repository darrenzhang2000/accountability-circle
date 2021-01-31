from django.urls import path, include
from . import views
urlpatterns = [

    # are okay, are implemented already (there's some things change yet)
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('displaymissions/', views.displayMissions, name='displaymissions'),


    # this need to be implemented
    path('settings/', views.edit, name='edit'),
    path('success/', views.sucess, name='sucess'),
    path('weekly/', views.weekly, name='weekly'),
    path('feedback/', views.feedback, name='feedback'),
    path('match/', views.match, name='match'),
]
