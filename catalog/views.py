from django.views.generic import FormView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import AddForm
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .mixins import AjaxFormMixin
from .models import Product 
from .resources import ProductResource 
from django.db.models import F

import time
import json

from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    products = Product.objects.all() #ordered alphabetically

    return render(request, 'catalog/index.html', {'products' : products})

@login_required
def supplyLow(request):
    products = Product.objects.order_by(F('stockQty') - F('minQty'))

    return render(request, 'catalog/index.html', {'products' : products})

@login_required
def take(request):
    form = AddForm();
    message = "take from"

    return render(request, 'catalog/add.html', {'form': form, 'message': message})

@login_required
def add(request):
    form = AddForm();
    message = "add to"

    return render(request, 'catalog/add.html', {'form': form, 'message': message}) 

@login_required
def export(request):
    product_resource = ProductResource() 
    dataset = product_resource.export()
    timestr = time.strftime("%Y-%m-%d")
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products-' + timestr + '.csv"'

    return response


@login_required
def search(request):
    if request.is_ajax() and request.method == "POST":
        query = request.POST.get('query', False)
        products = Product.objects.filter(description__icontains=query)[:20]
    else:
        query = ''

    return render(request, 'catalog/ajax_search.html', {'results' : products})

@login_required
def updateAdd(request):
    if request.is_ajax() and request.method == "POST":
        print(request)
        selectedItems = request.POST #json.loads(request.body)
        
        for code, quantity in selectedItems.items():
            print(code, quantity)
            try:
                item = Product.objects.get(code=code)
                item.stockQty = item.stockQty + int(quantity)
                item.save()
            except ObjectDoesNotExist:
                print("Cannot find item with a code " + code)
            except MultipleObjectsReturned:
                print("There are more than one items with a code " + code)

    return render(request, 'catalog/add.html')

@login_required
def updateTake(request):
    if request.is_ajax() and request.method == "POST":
        print(request)
        selectedItems = request.POST #json.loads(request.body)
        
        for code, quantity in selectedItems.items():
            print(code, quantity)
            try:
                item = Product.objects.get(code=code)
                item.stockQty = item.stockQty - int(quantity)
                item.save()
            except ObjectDoesNotExist:
                print("Cannot find item with a code " + code)
            except MultipleObjectsReturned:
                print("There are more than one items with a code " + code)

    return render(request, 'catalog/add.html')