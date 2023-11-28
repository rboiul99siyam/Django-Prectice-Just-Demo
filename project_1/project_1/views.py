from django.http import HttpResponse

def home(requset):
    return HttpResponse("This is Home Page Now !")
def contact(requst):
    return HttpResponse("This is contact page")

def About(requst):
    return HttpResponse("This is About section new !")