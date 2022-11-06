from django.contrib import admin
from .models import AnnouncementType, Announcement, Teacher, Room, Slot, Planning

admin.site.register(AnnouncementType)
admin.site.register(Announcement)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Slot)
admin.site.register(Planning)