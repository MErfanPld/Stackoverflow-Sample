from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import tasks
from permissions import IsSuperUserMixin


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')

    def post(self, request):
        pass


class BucketHome(IsSuperUserMixin, View):
    template_name = 'core/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects': objects})


class BucketDelete(IsSuperUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your request will done soon...', 'danger')
        return redirect('core:bucket')


class BucketDownload(IsSuperUserMixin, View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will start soon', 'warning')
        return redirect('core:bucket')
