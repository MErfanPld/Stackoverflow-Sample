from django.urls import path, include
from .views import UserRegister, UserLogin, UserLogout, UserDashboard
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

api_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', UserRegister.as_view(), name="register"),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_urls)),
]


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MjkyOTYwMiwiaWF0IjoxNjQyODQzMjAyLCJqdGkiOiI2NjQyMDU3Yjg1ZGY0NjNlODY3MTg2MTIwYTE5MWRiMCIsInVzZXJfaWQiOjJ9.dPWD98G1XhL_22WVZxZbMSGVwNQ2BLe3PaItOfhXeOw",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQyODQzNTAyLCJpYXQiOjE2NDI4NDMyMDIsImp0aSI6IjljN2U5OTAxNTdlYjQ1MTQ5YjQxOTFjYTFhYjI4ZDQzIiwidXNlcl9pZCI6Mn0.Xed-AoPRqOE1tJJ-F2G70Ekwx0f9z4kQ7OqgVZOZCBE"
# }
