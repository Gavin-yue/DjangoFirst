from django.shortcuts import render
from .models import Type
from .models import Goods
from .models import News
from django.http import Http404
from django.core.paginator import Paginator,PageNotAnInteger
from DjangoTest.settings import page_size

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
    news_list = News.objects.all()
    p=Paginator(news_list,page_size)
    number = p.num_pages
    page_range = p.page_range
    page = request.GET.get('page')
    print(page,type(page))
    try :
        page = int(page)
    except:
        page = 1
    if page > number or page <1:
        page = number

    data = p.page(page)
    if page <4:
        page_range=page_range[:4]
    elif page+4>number+1:
        page_range = page_range[-4:]
    else:
        page_range = page_range[page-2:page+2]
    return render(request,'new_html/news.html',{'news':news,'news_list':data,'number':number,'page_range':page_range})

def meishi_detail(request,id):
    goods = Goods.objects.filter(id=id)
    if goods.exists():
        good = goods[0]
    else:
        raise Http404
    return render(request,'new_html/meishi-con.html',{'good':good})

def news_detail(request,id):
    news = "nav-active"
    new = News.objects.filter(id=id)
    if new.exists():
        new = new[0]
    else:
        return Http404
    return render(request,'new_html/news-con.html' , {"news":news,"new":new})