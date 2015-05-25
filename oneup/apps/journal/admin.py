from django.contrib import admin

from .models import Journal, Category


class JournalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post title', {'fields': ['title']}),
        ('Url string', {'fields': ['slug']}),
        ('Date posted', {'fields': ['posted_date'], 'classes': ['collapse']}),
        ('Body', {'fields': ['body']}),
        ('Category', {'fields': ['category']}),
        ('Visible', {'fields': ['visible']}),
    ]
    list_display = ('title', 'posted_date', 'was_posted_recently')
    list_filter = ['posted_date']
    search_fields = ['title']

admin.site.register(Journal, JournalAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category name', {'fields': ['name']}),
        ('Url string', {'fields': ['slug']}),
        ('Category description', {'fields': ['description']}),
    ]
    list_display = ('name', 'slug')
    list_filter = ['slug']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
