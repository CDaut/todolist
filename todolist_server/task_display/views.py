from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_tasks_as_list(request):
    context = {'title': 'Tasklist',
               'fullname': request.user.first_name + request.user.last_name,
               'email': request.user.email}
    return render(request, 'task_display/task_list.html', context)


def redirect_to_list_view(request):
    return redirect('list/')
