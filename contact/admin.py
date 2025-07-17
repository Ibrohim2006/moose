from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_solved')
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('is_solved', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_solved',)
