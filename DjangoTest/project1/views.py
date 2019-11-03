from django.shortcuts import render
from .models import Type

# Create your views here.
def index(request):
    return render(request,'new_html/index.html')

def meishi(request):
    type_list = Type.objects.all()  #查询表中的所有数据
    print(type_list,type(type_list))
    print("=============================")
    return render(request,'new_html/meishi.html',{'type_list':type_list})

def base(request):
    return render(request,'base/base.html')

def inherint(request):
    return render(request,'base/inherint.html')

def inherint1(request):
    return render(request,'base\inherint_one.html')

def pinpai(request):
    return render(request,'new_html/pinpai.html')

# def meishi(request):
#     return render(request,'new_html/meishi.html')

def shop(request):
    return render(request,'new_html/shop.html')

def about_us(request):
    return render(request,'new_html/about-us.html')
def news(request):
    return render(request,'new_html/news.html')
