from importlib.resources import path
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def feed(request):
    return render(request, 'pages/feed.html')


def loginpage(request):
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'signuppage.html')


def register(request):

    if request.method == 'POST':

        first_name = request.POST['name1']
        last_name = request.POST['name2']
        age = request.POST['age']
        pnumber = request.POST['pnumber']
        address = request.POST['address']
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User.objects.create_user(
            email=email, username=email, password=password2, first_name=first_name, last_name=last_name)
        user.save()
        print("User Created")
        return redirect('/')

    else:
        return render(request, 'signuppage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        messages.info(request, "What are you doing!!!")
        return render(request, 'loginpage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})
