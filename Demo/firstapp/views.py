from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import Reservation
def hello_world(request):
    return HttpResponse("hello world")

class HelloIndia(View):
    def get(self, request):
        return HttpResponse("Hello India")
# Create your views here.

def home(request):
    form = Reservation()

    if request.method=='POST':
        form = Reservation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render(request, 'index.html',{'form':form})