from django.contrib import admin

from blogs.models import Category, Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = [
        'title',
        'author',
        'category',
    ]

    list_filter = [
        'author',
        'category',
    ]

    search_fields = [
        'title',
        'body'
    ]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
