from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageview(request):
    return HttpResponse("<h1>homepage for user appp</h1>")