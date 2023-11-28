from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def home(requst):
#     return HttpResponse("this first app home page !")

def home(requst):
    return render(requst , 'first_app/home.html')