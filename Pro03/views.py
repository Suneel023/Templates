from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse("Main Page of Django")

def html_demo(request):
    return render(request,"sample.html")

def html_demo2(request):
    return render(request,"sample2.html")