from django.shortcuts import render, HttpResponse


def homepage(request):
    return render(render, "index.html")


test(request):
    return render(request, "test.html")


def homepage(request):
    return HttpResponse("This is my first page")

def check(request):
    return HttpResponse("Текшерүү")

def test(request):
    return HttpResponse("Текст3")



