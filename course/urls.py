
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('<kurs_adı>/',views.details),
    path('kategori/<int:category_id>/',views.getCourseByCategoryId),
    path('kategori/<str:category_name>/',views.getCourseByCategory,name='course_by_category'),

]
