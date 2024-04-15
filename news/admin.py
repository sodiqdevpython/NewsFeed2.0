from django.contrib import admin
from .models import News, Types, ContactModel, CommentModel

@admin.register(News)
class NewsAdminView(admin.ModelAdmin):
    list_display = ['title', 'type', 'published', 'status']
    search_fields = ['title', 'body']
    list_filter = ['status']
    list_per_page = 5
    prepopulated_fields = {"slug": ['title']}

admin.site.register(Types)

@admin.register(ContactModel)
class ContactAdminView(admin.ModelAdmin):
    list_display = ['name', 'email', 'time']
    search_fields = ['name', 'email', 'body']

@admin.register(CommentModel)
class CommentModelAdminView(admin.ModelAdmin):
    list_display = ['user', 'comment_date']
    search_fields = ['user', 'comment_text']