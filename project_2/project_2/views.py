from django.shortcuts import render

def indexHere(request):
    return render(request , 'index.html')