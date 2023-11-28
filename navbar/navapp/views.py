from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(reqest):
    return render (reqest , './navigation/about.html')
def contact(request):
    # return render (request , './navigation/contact.html')
    return HttpResponse("This is a page !")