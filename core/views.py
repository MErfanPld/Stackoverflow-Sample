from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import tasks


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'core/home.html')

    def post(self, request):
        pass


class BucketHome(LoginRequiredMixin, View):
    template_name = 'core/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects': objects})


class BucketDelete(LoginRequiredMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your request will done soon...', 'danger')
        return redirect('core:bucket')
