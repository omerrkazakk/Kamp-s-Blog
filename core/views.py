from django.shortcuts import render
import core.models
import blog.models

def anasayfa (request):
    bloglar=blog.models.BlogPost.objects.all()

    context={
         "bloglar":bloglar
    }
    return render(request, "anasayfa.html",context)



def iletisim(request):
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
   