from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from task_display.forms import AddTaskForm
from api.models import Task, Category
from user_manager.models import ApplicationUser
import logging


def create_new_task(request):
    # get the associated app user
    appuser = ApplicationUser.objects.get(auth_user=request.user)
    cat = Category.objects.get(pk=request.POST.get('category'))

    if Task.objects.filter(title=request.POST.get('title')).count() != 0:
        return 'Task already exists'

    # create new Task
    task = Task.objects.create(
        title=request.POST.get('title'),
        created_by=appuser,
        category=cat,
        modifier_function=request.POST.get('modifier_function'),
        importance=request.POST.get('importance'),
        urgency=request.POST.get('urgency'),
        base_importance=request.POST.get('base_importance'),
    )

    # add all optional parameters
    if request.POST.get('description') != '':
        task.description = request.POST.get('description')

    if request.POST.get('due_date') != '':
        task.due_date = request.POST.get('due_date')

    if request.POST.get('modifier_function') != '':
        task.modifier_function = request.POST.get('modifier_function')

    if request.POST.get('m') != '':
        task.m = request.POST.get('m')

    if request.POST.get('exponent') != '':
        task.exponent = request.POST.get('exponent')

    task.save()

    logging.info(f'User {request.user.username} created task {task}')

    return True


# Create your views here.
@login_required
def list_tasks_as_list(request):
    context = {'title': 'Tasklist',
               'fullname': request.user.first_name + ' ' + request.user.last_name,
               'email': request.user.email,
               'username': request.user.username,
               'tasks': Task.objects.filter(created_by=ApplicationUser.objects.get(auth_user=request.user)),
               'categories': Category.objects.all()}
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
    # if a post request has been made, create a new task
    if request.method == 'POST':
        success = create_new_task(request)

        if success:
            context['success'] = f'Created task {request.POST.get("title")}'
        else:
            context['error'] = f'Task with name {request.POST.get("title")} already exists!'

    return render(request, 'task_display/add_task.html', context)


@login_required
def eisenhower_view(request):
    context = {'title': 'Eisenhower matrix',
               'fullname': request.user.first_name + ' ' + request.user.last_name,
               'email': request.user.email,
               'username': request.user.username,
               'tasks': Task.objects.filter(
                   created_by=ApplicationUser.objects.get(auth_user=request.user))
               }
    return render(request, 'task_display/eisenhower.html', context)
