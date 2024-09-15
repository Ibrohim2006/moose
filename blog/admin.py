from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    readonly_fields = ('slug',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
