from django.shortcuts import render


# Create your views here.
def login_view(request):
    if request.method == 'GET':
        context = {'title': 'Log-in'}
        return render(request, 'user_manager/login.html', context)
