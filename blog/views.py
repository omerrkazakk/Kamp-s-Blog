from django.shortcuts import render
import blog.models

def blog_list(request):
    return render(request, 'blog_list.html')
def blog_detay(request, id):
    try:
        yazi= blog.models.BlogPost.objects.get(id=id)
    except:
        return render(request, "404.html", status=404)
    context={
        'yazi':yazi
    }
    return render(request, 'blog_detay.html', context)

def blog_ekle(request):
    return render(request, 'blog_ekle.html')
def blog_sil(request, id):
    return render(request, 'blog_sil.html', {'id': id})
def blog_düzenle(request, id):
    return render(request, 'blog_düzenle.html', {'id': id})
