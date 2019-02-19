from django.db import models
import uuid # Required for unique book instances
from django.urls import reverse # Used to generate URLs by reversing the URL patterns




class Product(models.Model):

    '''Model Representing Product'''

    #Descriptiom of the product
    description = models.CharField(max_length=200)

    #Party
    party = models.CharField(max_length=20)

    #Vendor
    vendor = models.CharField(max_length=20)

    #Product Code
    code = models.CharField(max_length=20)

    #Price Unit
    priceUnit = models.CharField(max_length=10)

    #Actual Price
    actualPrice = models.DecimalField(max_digits=8, blank=True, null=True, decimal_places=2)

    #Units
    units = models.CharField(max_length=10)

    #Cost
    cost = models.DecimalField(max_digits=8, blank=True, null=True, decimal_places=2)

    #Min Quantity
    minQty = models.IntegerField(help_text='Enter minimum quantity')

    #Quantity in Stock
    stockQty = models.IntegerField(help_text='Enter current quantity in stock')

    #Quantity Unit
    unitQty = models.CharField(max_length=5)

    #Quantity to order
    orderQty = models.IntegerField(blank=True, null=True, help_text='OPTIONAL: Enter quantity to order')

    #Comments
    comments = models.TextField(max_length=300, blank=True, help_text='OPTIONAL: Enter Comments')

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)]) 

    class Meta:
        ordering = ['description']



class Party(models.Model):
    
    '''Model Representing Party'''

    name = models.CharField(max_length=20, help_text='Enter an ordering party (e.g. General, Anesthesia)')

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendor-detail', args=[str(self.id)])



class Vendor(models.Model):
    
    '''Model Representing Vendor'''

    name = models.CharField(max_length=20, help_text='Enter a Vendor (e.g. MCKESSON, SCHEIN)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendor-detail', args=[str(self.id)])







