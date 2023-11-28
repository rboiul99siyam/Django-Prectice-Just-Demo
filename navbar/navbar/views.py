from django.shortcuts import render

from django.http import HttpResponse


def home (request):
   return render(request , 'index.html')




# def home(request):
#    return HttpResponse("This Home page ")


# TEMPLATES

# templates   