from django.urls import path
from perfil import views

app_name = 'perfil'

urlpatterns = [
    path('', views.login_view, name="index"),
    path('perfil/login/', views.login_view, name="login"),
    path('perfil/create-perfil/', views.createPerfil, name="create-perfil"),
    path('perfil/update-perfil/', views.updatePerfil, name="update-perfil"),
    path('perfil/logout/', views.logOut_view, name="logout"),
]