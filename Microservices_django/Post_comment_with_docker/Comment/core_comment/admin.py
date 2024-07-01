from django.contrib import admin
from core_comment.models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'text']
    ordering = ['-id']
    
admin.site.register(Comment, PostAdmin)