from django.contrib import admin
from .models import Post, Comment, ReplyComment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'comment', 'created_at', 'status']
	list_filter = ['created_at']

class ReplyCommentAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'reply', 'created_at', 'status']
	list_filter = ['created_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)