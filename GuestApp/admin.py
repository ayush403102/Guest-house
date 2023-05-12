from django.contrib import admin

from .models import Guest, Booking, Room, Img

admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Img)