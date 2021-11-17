from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user_manager.forms import CreateUserForm


def handle_login_get(request, context):
    # check if user is logged in
    if request.user.__class__.__name__ != 'AnonymousUser':
        return redirect('tasklist')
    else:
        return render(request, 'user_manager/login.html', context)


def handle_login_post(request, context):
    # check if username and password have been supplied
    if not ('username' in request.POST and 'password' in request.POST):
        context['error'] = "Empty username or password"
        return render(request, 'user_manager/login.html', context)

    username = request.POST['username']
    password = request.POST['password']

    # authenticate user
    user = authenticate(request, username=username, password=password)

    # redirect to appropriate site depending if user is authenticated or not
    if user is not None:
        # log in the user
        login(request, user)

        # check if this login attempt has a next parameter
        next_url = request.POST['next'] if 'next' in request.POST else 'tasklist'
        # fix next_url sometimes being undefined because of js weirdness...
        next_url = 'tasklist' if next_url == 'undefined' else next_url

        # redirect appropriately
        return redirect(next_url)

    else:
        context['error'] = 'Invalid username or password'
        return render(request, 'user_manager/login.html', context)


# Create your views here.
def login_view(request):
    context = {'title': 'Log-in'}
    if request.method == 'GET':
        return handle_login_get(request, context)
    elif request.method == 'POST':
        return handle_login_post(request, context)


def redirect_to_login_view(request):
    return redirect('login')


@login_required
def adduser_view(request):
    context = {'title': 'Create new user',
               'fullname': request.user.first_name + ' ' + request.user.last_name,
               'email': request.user.email,
               'username': request.user.username,
               'form': CreateUserForm(),
               }
    return render(request, 'user_manager/adduser.html', context)
