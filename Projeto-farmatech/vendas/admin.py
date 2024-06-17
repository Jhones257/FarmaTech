from django.contrib import admin
from . import models
# Register your models here.

class ItemVendaInline(admin.TabularInline):
    model = models.ItemVenda
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]

admin.site.register(models.vendas, VendaAdmin)
admin.site.register(models.ItemVenda)