from django.contrib import admin

from .models import Category, Location, Post


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)


admin.site.register(Location, LocationAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date', 'author', 'category')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'


admin.site.register(Post, PostAdmin)
