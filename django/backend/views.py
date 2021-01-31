from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as logUser

# Create your views here.
def login(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        email = request.POST["email"]
        password = request.POST["psw"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            logUser(request, user)
            return HttpResponseRedirect("/")
        return render(
            request, "login.html", {"email": email, "password": password}
        )
    else:
        pass
    return render(request, "login.html")


def edit(request):
    if request.method == "POST":
        pass
    else:
        pass
    return HttpResponse("hi")
    return render(request, "name.html", {"form": form})


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
