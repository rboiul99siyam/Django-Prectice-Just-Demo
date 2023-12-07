from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index,name='homePage'),
    path('aboutPage/', views.about, name='aboutPage'),
    path('djangoForm/', views.passwordValidation, name='djangoForm'),
]
