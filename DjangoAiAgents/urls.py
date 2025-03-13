from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ai_agents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.agent_list, name='agent_list'),
    path('agent/<int:agent_id>/', views.agent_detail, name='agent_detail'),
]