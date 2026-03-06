from django.shortcuts import render

def blog_list(request):
    return render(request, 'blog_list.html')
def blog_detay(request, id):
    return render(request, 'blog_detay.html', {'id': id})
def blog_ekle(request):
    return render(request, 'blog_ekle.html')
def blog_sil(request, id):
    return render(request, 'blog_sil.html', {'id': id})
def blog_düzenle(request, id):
    return render(request, 'blog_düzenle.html', {'id': id})
