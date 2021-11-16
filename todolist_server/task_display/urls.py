from django.urls import path
from task_display.views import list_tasks_as_list, redirect_to_list_view

urlpatterns = [
    path('tasks/list/', list_tasks_as_list),
    path('tasks/', redirect_to_list_view),
]
