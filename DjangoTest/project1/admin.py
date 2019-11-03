from django.contrib import admin
from .models import Goods,Goods_type,Type
# Register your models here.

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','Type_name']
    ordering = ['id']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['goods_name',"price"]

@admin.register(Goods_type)
class Goods_TypeAdmin(admin.ModelAdmin):
    list_display = ['goods','type']

