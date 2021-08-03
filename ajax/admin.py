from django.contrib import admin
from .models import Post, PostImage


class ImagesAdminInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', )
    list_display_links = ('title', )
    readonly_fields = ('created_at', )
    inlines = [ImagesAdminInline, ]


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
