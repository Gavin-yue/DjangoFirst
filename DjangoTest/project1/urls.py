from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('meishi/', views.meishi),
    path('base/',views.base),
    path('inherint/',views.inherint),
    path('inherint1/',views.inherint1),
    path('pinpai/',views.pinpai),
    path('shop/',views.shop),
    path('about_us/',views.about_us),
    path('news/',views.news),

]

app_name = 'project1'