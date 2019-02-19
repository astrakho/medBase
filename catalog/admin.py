from django.contrib import admin

# Register your models here.

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from catalog.models import Product


@admin.register(Product)
#admin.site.register(Party)
#admin.site.register(Vendor)

class ProductAdmin(ImportExportModelAdmin):
    pass