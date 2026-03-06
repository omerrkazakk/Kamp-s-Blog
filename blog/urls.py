from django.urls import path
from.import views
urlpatterns=[
    path('' , views.blog_detay, name='blog_detay'),
    path('blog_düzenle/', views.blog_düzenle, name='blog_düzenle'),
    path('blog_ekle/', views.blog_ekle, name='blog_ekle'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_sil/', views.blog_sil, name='blog_sil'),
]

