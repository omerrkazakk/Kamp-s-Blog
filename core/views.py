from django.shortcuts import render
import core.models
import blog.models
from .models import ContactMessage  
from django.shortcuts import redirect
def anasayfa (request):
    bloglar=blog.models.BlogPost.objects.all()

    context={
         "bloglar":bloglar
    }
    return render(request, "anasayfa.html",context)



def iletisim(request):
    if request.method == "POST":
        
        ad_soyad = request.POST.get('full_name')
        email = request.POST.get('e_mail') 
        mesaj = request.POST.get('message')
        
       
        ContactMessage.objects.create(
            full_name=ad_soyad,
            e_mail=email,       
            message=mesaj
        )
        
        return redirect('iletisim')
        
    return render(request, 'iletisim.html')


def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def yazarlar(request):
    yazar_list=blog.models.Author.objects.all()

    context = {
        "yazarlar": yazar_list,
        "title": "Yazarlar",
        "yazarlar_sayi": len(yazar_list),
        
    }

    return render(request, 'yazarlar.html', context)
def yazar_detay(request,id):
    try:
        yazar=blog.models.Author.objects.get(id=id)
    except:
        return render(request,"404.html",status=404)

    context={
        "author":yazar
    }
    return render(request,"yazar_detay.html",context)