from django.urls import path

from . import views

#from catalog.views import AddFormView

urlpatterns = [
    path('', views.index, name='index'),
    path('supplyLow/', views.supplyLow, name='supplyLow'),
    path('take/', views.take, name='take'),
    path('add/', views.add, name='add'), 
    path('export/', views.export, name='export'),
    path('updateAdd/', views.updateAdd, name='updateAdd'),
    path('updateTake/', views.updateTake, name='updateTake'),
    path('search/', views.search, name='search'),
]