from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hello_world(request):
    return HttpResponse("hello world")

class HelloIndia(View):
    def get(self, request):
        return HttpResponse("Hello India")
# Create your views here.

