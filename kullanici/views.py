from django.shortcuts import render

# Create your views here.
def cikisyap(request):
    return render(request, 'cikis_yap.html')
def girisyap (request):
    return render(request, 'girisyap.html')
def profil (request):
    return render(request, 'profil.html')
def kayitol (request):
    return render(request, 'kayit_ol.html')