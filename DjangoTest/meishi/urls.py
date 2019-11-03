from django.urls import path,include
from . import views

urlpatterns = [
    path('index1/',views.index1),
]
app_name = "meishi1"