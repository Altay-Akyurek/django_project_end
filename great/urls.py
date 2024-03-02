from django import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('kurs/',include('course.urls')),
    path('',include('transitions.urls')),
    path('account/',include('account.urls')), 
    path('admin/', admin.site.urls),
]
