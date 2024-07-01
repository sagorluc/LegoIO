from django.contrib import admin
from core_post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'comments']
    ordering = ['-id']
    
admin.site.register(Post, PostAdmin)
