from django.urls import path
from django.contrib.auth import views as auth_views
from TeamBuilderApp.views import index, registration_view, main, logout_user, room

urlpatterns = [
    path('', index, name='index'),
    path('login', auth_views.LoginView.as_view(template_name= 'Team/login.html'), name='login'),
    path('register', registration_view, name='register'),
    path('mainpage', main, name='main'),
    path('<str:room_name>/', room, name='room'),
    path("logout", logout_user, name="logout"),
]