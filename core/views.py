from django.shortcuts import render
import core.models

def anasayfa (request):
    return render(request, "anasayfa.html")



def iletisim(request):
    return render(request, 'iletisim.html')


def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def yazarlar(request):
    author =[ 
    core.models.Author(
    full_name="Ömer Kazak",
    title="Backend Developer",
    bio="Python ve Django İle Web Uygulamaları Geliştiriyor.",
    profile_url="#"
    ),

    core.models.Author(
    full_name="Miraç İmece",
    title="Frontend Developer",
    bio="Html ve Css İle Web Siteleri Geliştiriyor.",
    profile_url="#"
    ),
     core.models.Author(
    full_name="Atacan Şahin",
    title="Syber Security",
    bio="Siber Güvenlik Alanında Çalışıyor.",
    profile_url="#"
    ),
 core.models.Author(
    full_name="Emin Karaman",
    title="Full Stack Developer",
    bio="Html ve Css İle Web Siteleri Geliştiriyor,Django İle Dinamik Web Uygulamaları Yapıyor",
    profile_url="#"
    ),
 core.models.Author(
    full_name="Mirsad Bakır",
    title="Game Developer",
    bio="Unity ile İle Oyun Geliştiriyor.",
    profile_url="#"
    ),
 core.models.Author(
    full_name="Said Karakaş",
    title="Ai Developer",
    bio="Yapay Zeka İle İlgileniyor.",
    profile_url="#"
    )

    ]

    context = {
        "yazarlar": author,
        "title": "Yazarlar",
        "yazarlar_sayi": len(author)
    }

    return render(request, 'yazarlar.html', context)