from django.shortcuts import render
from .models import Type
from .models import Goods
from django.http import Http404

# Create your views here.
def index(request):
    index = "nav-active"
    return render(request,'new_html/index.html',{"index":index})

def meishi(request):
    meishi1 = "nav-active"
    type_list = Type.objects.all()  #查询表中的所有数据
    # type_list1 = Type.objects.filter(id=3)
    # type_list1 = Type.objects.get(id=3)
    # type_list1 = Type.objects.exclude(id=3)
    # type_list1 = Type.objects.exclude(id=3).exclude(Type_name = "风味披萨")
    # type_list1 = Type.objects.filter(id__lt=3)
    # type_list1 = Type.objects.filter(id__gte=3)
    # type_list1=Type.objects.filter(Type_name__contains="风")
    # type_list1=Type.objects.filter(Type_name__startswith="风")
    # type_list1=Type.objects.filter(Type_name__endswith="排")
    type_list1 = Type.objects.order_by("-id")
    if type_list1.exists():
        print("有数据")
    else:
        print("无数据")


    print(type_list1,type(type_list1))
    # print(type_list,type(type_list))
    print("=============================")
    return render(request,'new_html/meishi.html',{'type_list':type_list,"meishi1":meishi1})

def base(request):
    index="nav-active"
    return render(request,'base/base.html',{"index":index})

def inherint(request):
    return render(request,'base/inherint.html')

def inherint1(request):
    return render(request,'base\inherint_one.html')

def pinpai(request):
    pinpai = "nav-active"
    return render(request,'new_html/pinpai.html',{'pinpai':pinpai})

# def meishi(request):
#     return render(request,'new_html/meishi.html')

def shop(request):
    shop = "nav-active"
    return render(request,'new_html/shop.html',{"shop":shop})

def about_us(request):
    about_us="nav-active"
    return render(request,'new_html/about-us.html',{"about_us":about_us})
def news(request):
    news = "nav-active"
    return render(request,'new_html/news.html',{'news':news})

def meishi_detail(request,id):
    goods = Goods.objects.filter(id=id)
    if goods.exists():
        good = goods[0]
    else:
        raise Http404
    return render(request,'new_html/meishi-con.html',{'good':good})