from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_id', 'to_show', 'created_at', 'updated_at',)


admin.site.register(Event, EventAdmin)