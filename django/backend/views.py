from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as logUser
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Mission
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

def display_goals(request):

    your_goals = [
        {
            "date": "01-30-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-07-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-14-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "02-21-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-01-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-07-2021",
            "goal": "Do 15 LeetCode questions"
        }
    ]


    partner_goals = [
        {
            "date": "01-30-2021",
            "goal": "Do 3 LeetCode questions"
        },
        {
            "date": "02-07-2021",
            "goal": "Do 3 LeetCode questions"
        },
        {
            "date": "02-14-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-21-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "03-01-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-07-2021",
            "goal": "Do 15 LeetCode questions"
        }
    ]

    return render(request, "goalTables.html", {"your_goals":your_goals,"partner_goals":partner_goals})


def match(request):
    """ Match the user against another one """

    return HttpResponse("Sent")

def new_weekly(request):
    return render(request, 'new_feedback.html')





def weekly(request):
    return render(request,'feedback.html')


    """ The user is going to set his weekly Goals"""
    pass
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    else:
        return HttpResponse("Method not Allowed")



def success(request):

    return render(request, "success.html")

def feedback(request):

    return render(request, "feedback.html")
    pass
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    else:
        return HttpResponse("Method not Allowed")
