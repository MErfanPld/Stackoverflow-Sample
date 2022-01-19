from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, UserDashboard

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', UserDashboard.as_view(), name='dashboard'),
]
