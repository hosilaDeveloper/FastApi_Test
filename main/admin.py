from django.contrib import admin
from .models import Category, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title', 'category', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
