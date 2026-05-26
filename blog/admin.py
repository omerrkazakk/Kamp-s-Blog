from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import BlogPost, Author


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ("title", "author", "created_at") 
    search_fields = ("title",)
    list_filter = ("created_at",)

@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ("full_name", "title")
    search_fields = ("full_name", "title")