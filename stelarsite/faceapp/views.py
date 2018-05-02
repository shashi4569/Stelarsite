from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Stelar, you are at the Face App page")