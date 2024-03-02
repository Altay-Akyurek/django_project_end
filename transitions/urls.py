from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('hakkında/',views.hakkında),
    path('haber/',views.haber),
    path('son_Bagisler/',views.son_bagışlar),
    path('sss/',views.sss),
    path('iletisim/',views.iletisim),
    path('uyelik/', views.uyelik, name='uyelik'),
]

