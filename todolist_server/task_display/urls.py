from django.urls import path
from task_display.views import list_tasks_as_list

urlpatterns = [
    path('tasks/list/', list_tasks_as_list),
]
