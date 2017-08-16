from django.contrib import admin

from blog.models import Blog, BlogPost, BlogSection, SectionSection, CommentBlogPost, ReplyComment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'theme')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titre','date_post')

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogSection)
admin.site.register(SectionSection)
admin.site.register(CommentBlogPost)
admin.site.register(ReplyComment)