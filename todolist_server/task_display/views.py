from django.shortcuts import render


# Create your views here.
def list_tasks_as_list(request):
    return render(request, 'task_display/task_list.html')
