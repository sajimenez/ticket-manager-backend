from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created', 'creator', )
    list_filter = ('status', )
    search_fields = ('id', 'title', )
    ordering = ('-created', )


admin.site.register(Ticket, TicketAdmin)
