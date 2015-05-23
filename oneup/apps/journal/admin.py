from django.contrib import admin

from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['posted_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'posted_date', 'was_posted_recently')
    list_filter = ['posted_date']
    search_fields = ['title']

admin.site.register(Journal, JournalAdmin)
