from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course(reqest):
    return HttpResponse("This is course Page now !")

def Salary(request):
    return HttpResponse("This is Salary Here Now !")
