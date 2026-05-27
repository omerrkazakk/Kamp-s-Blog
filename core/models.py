from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    profile_url = models.URLField(blank=True , null=True)

    def __str__(self):
        return self.full_name
    

from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100) 
    e_mail = models.EmailField()                
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name