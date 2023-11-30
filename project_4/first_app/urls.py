from django.urls import path ,include

from . import views
urlpatterns = [
    path('index/', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('contact/<int:id>/', views.contact, name='contact')

]