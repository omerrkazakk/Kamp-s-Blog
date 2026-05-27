from django.urls import path
from.import views
urlpatterns=[
    path('' , views.anasayfa, name='anasayfa'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('hakkimizda/', views.hakkimizda,name='hakkimizda'),
    path('yazarlar/', views.yazarlar,name='yazarlar'),
    path('yazar_detay/<int:id>/',views.yazar_detay,name="yazar_detay")
]



