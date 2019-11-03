from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('meishi/', views.meishi),
    path('base/',views.base),
    path('inherint/',views.inherint),
    path('inherint1/',views.inherint1),

]

app_name = 'project1'