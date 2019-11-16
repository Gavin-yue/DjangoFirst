from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index,name = "index"),
    path('meishi/', views.meishi,name = "meishi"),
    path('base/',views.base,name ="base"),
    path('inherint/',views.inherint,name = "inherint"),
    path('inherint1/',views.inherint1,name = "inherint1"),
    path('pinpai/',views.pinpai,name = "pinpai"),
    path('shop/',views.shop,name = "shop"),
    path('about_us/',views.about_us,name = "about_us"),
    path('news/',views.news,name = "news"),
    # path('meishi_detail/<int:id>',views.meishi_detail,name = "meishi_detail"),
    path('meishi_detail/(?p <id>)',views.meishi_detail,name = "meishi_detail"),
    path('news_detail/<int:id>',views.news_detail,name="news_detail"),

]

app_name = 'project1'