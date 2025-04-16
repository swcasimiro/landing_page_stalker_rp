from django.contrib import admin
from django.contrib import admin
from .models import News, Tag

admin.site.register(Tag)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'views_count')
    list_filter = ('is_published', 'tags')
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ('title',)}

    def views_count(self, obj):
        return obj.views

    views_count.short_description = 'Просмотры'
