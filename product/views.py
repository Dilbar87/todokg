from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("This is my first page")



