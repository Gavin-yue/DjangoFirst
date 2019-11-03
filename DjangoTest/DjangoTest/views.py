from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def index(request):   #
    num1 = 12
    str1 = "hello,yuetao!"
    list1 = [1,3,2,4]
    tup1 = (9,8,0,5)
    dict1 = {"name":"yuetao",'age':25}
    set1 = {'wang','li','zhang','wu'}

    # return HttpResponse("Hello world!",)
    return render(request,'index.html',locals())


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        print(username,pwd)
        if username == 'admin' and pwd == "admin":
            return HttpResponseRedirect('/index')


    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        pwd1 = request.POST.get("password")
        print(username1,pwd1)
        return HttpResponseRedirect('/login')
    return render(request,'register.html')