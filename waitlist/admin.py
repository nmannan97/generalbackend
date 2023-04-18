# Register your models here.
from django.contrib import admin
from .models import waitlist
class waitlistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['email']}),
        (None,               {'fields': ['phonenumber']}),
        (None,               {'fields': ['position']}),
    ]
    list_display = ('name', 'email', 'phonenumber', 'position')
admin.site.register(waitlist, waitlistAdmin)