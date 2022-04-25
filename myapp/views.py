
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import profile
# Create your views here.
flag = 0
def index(request):
    # print("you are entered into INDEX")
    # print("flag is: ",flag)
    # print("Value of username is: ",request.User.username)
    
    if (not (request.user.username)):
        # print("NO bro")
        return render(request, 'index.html')

    # if (request.user.username is not None):
    if (request.user.username):
        # print("1/2 YES bro")
        profiles = profile.objects.get(Email=request.user.username)
        context = {'profile': profiles}
        # print("YES bro")
        return render(request, 'index.html',context)
    else:
        return render(request, 'index.html')
    # # return render(request, 'index.html')

def feed(request):
    return render(request, 'pages/feed.html')

def profilepage(request):
        if (not (request.user.username)):
            return render(request, 'pages/profile.html')
        if (request.user.username):
            profiles = profile.objects.get(Email=request.user.username)
            context = {'profile': profiles}
            return render(request, 'pages/profile.html',context)
        else:
            return render(request, 'pages/profile.html')

    


def loginpage(request):
    return render(request, 'loginpage.html')


def signup(request):
    return render(request, 'signuppage.html')


def register(request):

    if request.method == 'POST':

        name1 = request.POST['name1']
        name2 = request.POST['name2']
        age = request.POST['age']
        pnumber = request.POST['pnumber']
        address = request.POST['address']
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        user = User.objects.create_user(username = email, password = password2, email = email)
        user.save()
        user_model = profile(First_name=name1, Last_name=name2, Age=age , Email= email ,Contact_no=pnumber, Password=password2).save()
        print("Before User Created")

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
            flag = 1
            # print("flag at login is: ",flag)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        messages.info(request, "What are you doing!!!")
        return render(request, 'loginpage.html')

def logout(request):
    auth.logout(request)
    flag = 0
    request.user.username = None
    print("username is: ",request.user.username)
    print("flag is: ",flag)
    return redirect('/')
    # return render(request, 'index.html')


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})
