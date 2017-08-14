from django.contrib import admin

from blog.models import Blog, BlogPost

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('auteur',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titre','date_post')

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)