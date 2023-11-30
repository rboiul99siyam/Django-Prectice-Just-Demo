from django.shortcuts import render

# Create your views here.

def home (request):
    d = {

        'author' : 'Rohim', 'age' : 20 , 'lst' : [ 1,2,3,4],
        'course' : [
            {
                'id' : 1,
                "name" : 'python',
                'fee' : 5000

            },
            {
                'id' : 2,
                "name" : 'c++',
                'fee' : 2000

            },
            {
                'id' : 3,
                "name" : 'c',
                'fee' : 3000

            },
            {
                'id' : 4,
                "name" : 'django',
                'fee' : 4000

            }
        ]
    }
    return render(request,'home.html', d)

def contact(reqeust):
    d = {
        'Student ' : [
            {
                'name' : 'Ab : rohim',
                'roll' :1,
                'address':'chandpur',
            },
            {
                'name' : 'Ab : Korim',
                'roll' :2,
                'address':'chandpur,foridgong',
            },
        ]
    }
    return render(reqeust , 'contact.html' , d)