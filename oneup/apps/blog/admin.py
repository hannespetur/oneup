from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post title', {'fields': ['title']}),
        ('Url string', {'fields': ['slug']}),
        ('Date information',
            {
                'fields': ['post_date', 'edited_date'],
                'classes': ['collapse']
            }
        ),
        ('Post body', {'fields': ['body']}),
        ('Visible', {'fields': ['body']}),
        ('Category', {'fields': ['visible']}),
    ]
    inlines = [ChoiceInline]
    list_display = (
        'title',
        'post_date',
        'category',
        'was_published_recently',
        'was_changed_recently'
    )
    list_filter = ['post_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
