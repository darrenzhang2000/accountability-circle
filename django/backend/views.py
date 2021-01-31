from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as logUser
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["psw"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            logUser(request, user)
            return HttpResponseRedirect(reverse('edit'))
        return render(
            request, "login.html", {"email": email, "password": password}
        )
    return render(request, "login.html")


def edit(request):
    if request.method == "POST":
        pass
    else:
        pass
    return render(request, "missionSetting.html")


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
