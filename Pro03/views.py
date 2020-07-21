from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("Main Page of Django")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"webpages/second.html")
