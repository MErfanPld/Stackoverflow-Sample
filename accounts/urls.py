from django.urls import path, include
from .views import UserRegister, UserLogin, UserLogout, UserDashboard
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'accounts'

api_urls = [
    path('token-auth/', obtain_auth_token)
]

urlpatterns = [
    path('register/', UserRegister.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_urls)),
]
