from django.urls import path
from .views import Home, BucketHome, BucketDelete

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('bucket/', BucketHome.as_view(), name="bucket"),
    path('bucket-delete/<key>/', BucketDelete.as_view(), name="bucket-delete"),
]
