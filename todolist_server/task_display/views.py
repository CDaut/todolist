from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task_display.forms import AddTaskForm


# Create your views here.
@login_required
def list_tasks_as_list(request):
    context = {'title': 'Tasklist',
               'fullname': request.user.first_name + ' ' + request.user.last_name,
               'email': request.user.email,
               'username': request.user.username}
    return render(request, 'task_display/task_list.html', context)


def redirect_to_list_view(request):
    return redirect('tasklist')


@login_required
def add_task_view(request):
    context = {'title': 'New task',
               'fullname': request.user.first_name + ' ' + request.user.last_name,
               'email': request.user.email,
               'username': request.user.username,
               'form': AddTaskForm()}
    return render(request, 'task_display/add_task.html', context)
