from django.shortcuts import render

# from django.http import HttpResponse
def About(request):
    return render(request , './navigation/about.html')

def profile(request):
#    return HttpResponse("this here Profile")
    return render(request , './navigation/profile.html')