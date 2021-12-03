from django.urls import path
from task_display.views import list_tasks_as_list, redirect_to_list_view, add_task_view, eisenhower_view, \
    add_category_view

urlpatterns = [
    path('tasks/list/', list_tasks_as_list, name='tasklist'),
    path('tasks/add/', add_task_view, name='add_task'),
    path('tasks/eisenhower/', eisenhower_view, name='eisenhower'),
    path('tasks/', redirect_to_list_view),
    path('categories/add/', add_category_view, name='add_category'),
    path('', redirect_to_list_view),
]
