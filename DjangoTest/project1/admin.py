from django.contrib import admin
from .models import Goods,Goods_type,Type,News
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

class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_name','image','date')
admin.site.register(News,NewsAdmin)

admin.site.site_header='贵族时代后台管理'  #控制登录页面和站点主题名称
admin.site.site_title='贵族时代'		#作用等同于html中的title标签