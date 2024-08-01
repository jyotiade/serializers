from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_list',stu_list,name="stu")
]