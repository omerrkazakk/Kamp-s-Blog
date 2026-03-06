from django.shortcuts import render

def anasayfa (request):
    return render(request, "anasayfa.html")



def iletisim(request):
    return render(request, 'iletisim.html')


def hakkimizda(request):
    return render(request, 'hakkimizda.html')