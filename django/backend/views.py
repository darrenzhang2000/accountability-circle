from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as logUser
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Mission
from . import Credentials
from django.core.mail import send_mail


# Create your views here.
def register(request):
    """ Registration of new User """

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["psw"]
        password_confirmation = request.POST["psw-repeat"]

        # verifications
        if password != password_confirmation:
            return render(
                request, "register.html", {"error": "The passwords do not Match"}
            )
        try:
            user = User.objects.create_user(
                username=email, email=email, password=password
            )
            user.save()
        except IntegrityError:
            return render(
                request, "register.html", {"error": "This Email is Taken already"}
            )

        # registration sucessfull, logs user and redirects to edit
        logUser(request, user)
        return HttpResponseRedirect(reverse("edit"))

    return render(request, "register.html")


def login(request):
    """ Login """

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["psw"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            logUser(request, user)
            return HttpResponseRedirect(reverse("edit"))
        return render(request, "login.html", {"email": email, "password": password})
    return render(request, "login.html")


def edit(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, "missionSetting.html")


def displayMissions(request):
    mission = Mission.objects.all()
    return render(request, "missionCategories.html", {"missions": mission})


def match(request):
    """ Match the user against another one """
    send_mail(
        'Subject here',
        'Here is the message.',
        Credentials.credentials['email'],
        ['daniel.passy@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Sent")



def weekly(request):
    pass
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    else:
        return HttpResponse("Method not Allowed")


def feedback(request):

    return render(request, "feedback.html")
    pass
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    else:
        return HttpResponse("Method not Allowed")
