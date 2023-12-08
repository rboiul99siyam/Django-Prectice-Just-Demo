from django.urls import path
from .views import delete_st
from . import views
urlpatterns = [
    path('', views.home),

]