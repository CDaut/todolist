from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user_manager.forms import CreateUserForm
from api.models import ApplicationUser


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
        next_url = 'tasklist' if '/' not in next_url else next_url

        # redirect appropriately
        return redirect(next_url)

    else:
        context['error'] = 'Invalid username or password'
        return render(request, 'user_manager/login.html', context)


def handle_adduser_get(request, context):
    return render(request, 'user_manager/adduser.html', context)


def handle_adduser_post(request, context):
    # check if user already exists
    if User.objects.all().filter(username=request.POST['username']).count() != 0:
        context['error'] = 'A user named "' + request.POST['username'] + '" already exists.'
        return render(request, 'user_manager/adduser.html', context)
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'],
                                        first_name=request.POST['first_name'],
                                        last_name=request.POST['last_name'])
        # also create the corresponding ApplicationUser
        ApplicationUser.objects.create(auth_user=user)

        # TODO: Maybe not display this as an error...
        context['error'] = 'User "' + request.POST['username'] + '" has been created!'
        return render(request, 'user_manager/adduser.html', context)


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
               'fullname': request.user.get_full_name(),
               'email': request.user.email,
               'username': request.user.username,
               'form': CreateUserForm(),
               }
    if request.method == 'GET':
        return handle_adduser_get(request, context)
    elif request.method == 'POST':
        return handle_adduser_post(request, context)


def logout_view(request):
    logout(request)
    return redirect('login')
