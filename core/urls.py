from django.urls import path
from.import views
urlpatterns=[
    path('' , views.anasayfa, name='anasayfa'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('hakkimizda/', views.hakkimizda,name='hakkimizda')
]



