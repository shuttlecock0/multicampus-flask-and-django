from django.contrib import admin
from .models import Board, Comment
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'content', 'created_at', 'updated_at',]
admin.site.register(Board, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'board_id']
admin.site.register(Comment, CommentAdmin)
