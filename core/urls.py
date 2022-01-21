from django.urls import path, include
from .views import Home, BucketHome, BucketDelete, BucketDownload
from . import api_views

app_name = 'core'


api_urls = [
    path('questions/', api_views.QuestionView.as_view()),
    path('questions/<int:pk>/', api_views.QuestionView.as_view()),
]

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('bucket/', BucketHome.as_view(), name="bucket"),
    path('bucket-delete/<str:key>/', BucketDelete.as_view(), name="bucket-delete"),
    path('bucket_download/<str:key>/', BucketDownload.as_view(), name='bucket_download'),
    path('api/', include(api_urls))
]
