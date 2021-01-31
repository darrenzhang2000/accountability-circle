from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/thanks/')
        return render(request, 'name.html', {'form': form})
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})

def edit(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return HttpResponse("hi")
    return render(request, 'name.html', {'form': form})


def weekly(request):
    pass
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    else:
        return HttpResponse('Method not Allowed')


def feedback(request):


    return render(request, 'backend/feedback.html')
    pass
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    else:
        return HttpResponse('Method not Allowed')
