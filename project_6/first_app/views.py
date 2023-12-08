from django.shortcuts import render ,redirect
from . import models
# Create your views here.
def home(res):
    student = models.Student.objects.all()
    return render(res,'home.html',{'data':student})

def delete_st(res,roll):
    st = models.Student.objects.get(roll).delete()
    return redirect('')