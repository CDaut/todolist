from django.urls import path, include
from user_manager.views import login_view

urlpatterns = [
    path('login/', login_view)
]
