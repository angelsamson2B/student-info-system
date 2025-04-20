from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from students import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
    'accounts/login/',
    auth_views.LoginView.as_view(template_name='students/login.html'),
    name='login'
    ),
]