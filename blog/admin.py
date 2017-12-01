from django.contrib import admin
from blog.models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title','timestamp')

    class Media:
        js = (
            '/static/js/kindeditor/kindeditor-all.js',
            '/static/js/kindeditor/lang/zh-CN.js',
            '/static/js/kindeditor/config.js',
        )

admin.site.register(BlogPost,BlogPostAdmin)