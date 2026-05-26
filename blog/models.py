from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)  
    bio = models.TextField()
    profile_url = models.CharField(max_length=200, default='http://127.0.0.1:8000/yazarlar/')

    def __str__(self):
        return self.full_name



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    static_url = models.CharField(max_length=200, default='img/default.png')

    def __str__(self):
        return self.title