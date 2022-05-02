from django.contrib import admin
from .models import Post, Pricing, Service


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'discrition', 'author', 'date_created', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('date_created', 'is_published')
    search_fields = ('id', 'title', 'discrition')
    list_display_links = ('id', 'title')


admin.site.register(Pricing)
admin.site.register(Service)
