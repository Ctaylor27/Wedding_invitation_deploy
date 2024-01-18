from django.contrib import admin
from .models import RSVP, Attendee
# Register your models here.


class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 1

class RSVPAdmin(admin.ModelAdmin):
    inlines = [AttendeeInline]
    list_display = ['name', 'party_total']
    search_fields = ['name']

    def party_total(self, obj):
        return obj.attendee_set.count()

    party_total.short_description = 'Number of Attendees'

admin.site.register(RSVP, RSVPAdmin)