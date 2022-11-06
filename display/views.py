from django.shortcuts import render
from django.utils import timezone,formats
from .models import Announcement

def display(request):

    # Get announcements
    announcements = Announcement.objects.all()

    context = {
        'organization_name': 'Lycée Georges Brassens',
        'announcements': announcements,
    } 
    return render(request, 'display/display.html', context)