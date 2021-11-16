from django.shortcuts import render


# Create your views here.
def login_view(request):
    context = {'title': 'Log-in'}
    return render(request, 'user_manager/login.html', context)
