from django.contrib import admin
from .models import Shop
# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude','longitude' ]

admin.site.register(Shop, ShopAdmin)

# admin.site.register(Shop)



