from django.urls import path
from.import views
urlpatterns=[
    path('cikisyap/' , views.cikisyap, name='cikisyap'),
    path('girisyap/', views.girisyap, name='girisyap'),
    path('kayitol/', views.kayitol,name='kayıtol'),
    path('', views.profil,name='profil')
]

