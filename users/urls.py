from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('home/', views.home, name='home'),
    path('all/',views.user_list, name='user-list'),
    path('delete/<int:id>/', views.delete_user, name='delete-user')
]
