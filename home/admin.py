from django.contrib import admin
from .models import Topic, Comment, Reply_to_Comment
# Register your models here

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('author',)

    class Meta:
        model = Topic

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author', 'created_at')
    list_display_links = ('id', 'content', 'author', 'created_at')
    search_fields = ('content', 'author')
    list_filter = ('author', 'created_at')

    class Meta:
        model = Comment

class Replies(admin.ModelAdmin):
    list_display = ('id', 'author',  'comment', 'created_at')

    class Meta:
        model = Reply_to_Comment


# Registering models with their respective admin classes
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply_to_Comment, Replies)