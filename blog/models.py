from django.db import models

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    summary=models.CharField(max_length=300)
    content=models.TextField()
    author_name=models.CharField(max_length=100)

    views=models.IntegerField(default=0)

    created_at=models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)
    static_url=models.CharField(max_length=200,default='img/default.png')
    def __str__(self):
        return self.title

