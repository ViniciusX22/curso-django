from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, dashboard, edit

app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastra-se/', register, name='register'),
    path('editar/', edit, name='edit'),
    path('sair/', auth_views.LogoutView.as_view(next_page='core:home'), name='logout')
]
