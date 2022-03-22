from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('akademik/',views.manage_akademik,name='manage_akademik'),
    path('edit_akademik/',views.edit_akademik,name='edit_akademik'),
    path('data_akademik/',views.data_akademik,name='data_akademik'),
]

