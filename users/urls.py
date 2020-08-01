from django.urls import path, include
from users.views import dashboard, register, index, home

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('', index, name='index'),
    path('oauth/', include('social_django.urls')),
]
