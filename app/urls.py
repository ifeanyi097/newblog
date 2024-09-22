from django.urls import path
from .views import index, superi

urlpatterns = [
    path('', index, name='index'),
    path('super/', superi, name='super'),

]