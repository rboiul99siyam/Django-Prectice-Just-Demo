from django.shortcuts import render
from .forms import contactForm , passwordValidationProject
# Create your views here.
def index(res):
    return render(res,'index.html')
def about(res):
    print(res.POST)
    if res.method == "POST":
        name = res.POST.get('userName')
        email = res.POST.get('email')
        selcet = res.POST.get('select')
        return render(res,'about.html',{'name':name,'email':email,'selcet':selcet})
    else:
        return render(res,'about.html')

def djangoForm(res):
    if res.method == "POST":
        form = contactForm(res.POST, res.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as des:
            #     for chunk in file.chunks():
            #         des.write(chunk)
            print(form.cleaned_data)
        # return render(res, 'djangoForm.html', {'form': form})
    else:
        form = contactForm()
    return render(res, 'djangoForm.html', {'form': form})

def passwordValidation(res):
    if res.method == "POST":
        form = passwordValidationProject(res.POST, res.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as des:
            #     for chunk in file.chunks():
            #         des.write(chunk)
            print(form.cleaned_data)
        # return render(res, 'djangoForm.html', {'form': form})
    else:
        form = passwordValidationProject()
    return render(res, 'djangoForm.html', {'form': form})

