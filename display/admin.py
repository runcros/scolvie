from django.contrib import admin
from .models import AnnouncementType, Announcement

admin.site.register(AnnouncementType)
admin.site.register(Announcement)