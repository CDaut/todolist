from django.urls import path, include
from user_manager.views import login_view, adduser_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('adduser/', adduser_view, name='adduser'),
]
