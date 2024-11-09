from django.shortcuts import render,redirect


def Home(request):
    return render(request,'Student/home.html')