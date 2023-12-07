from django import forms
from django.core import validators
class contactForm(forms.Form):
    name = forms.CharField(label='user Name :',widget= forms.TextInput(attrs={'placeholder':'Enter Your name : '}), validators=[validators.MinLengthValidator(10,message='Name of 10 must be use ')])
    email = forms.EmailField(label='user email : ',widget= forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),validators=[validators.EmailValidator('Plaese Enter a valid Email ')])
    age = forms.IntegerField(validators=[validators.MinValueValidator(20, message='must be 24 years old'),validators.MaxValueValidator(45, message='Your age over now ')])
    # weight = forms.DecimalField()
    # balance = forms.DecimalField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # check = forms.BooleanField()
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    Size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL = [('Apple','Apple'),('Boll','Boll'),('Cap','Cap')]
    Meals = forms.MultipleChoiceField(choices=MEAL , widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = cleaned_data['name']
    #     valEmail = cleaned_data['email']
    #     if len(valName) < 10:
    #         raise forms.ValidationError('Name  must be 10 charters ')
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('You must be use .com')

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='You have must 15 charters')])
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPass = cleaned_data['password']
        valRepass = cleaned_data['re_password']
        if  valPass != valRepass:
            raise forms.ValidationError('Password doesn,t match !')
        