from django.urls import path
from .views import Home, BucketHome, BucketDelete, BucketDownload

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('bucket/', BucketHome.as_view(), name="bucket"),
    path('bucket-delete/<str:key>/', BucketDelete.as_view(), name="bucket-delete"),
    path('bucket_download/<str:key>/', BucketDownload.as_view(), name='bucket_download'),
]
