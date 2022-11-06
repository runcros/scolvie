from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class AnnouncementType(models.Model):
    type = models.CharField(max_length=20, validators=[RegexValidator('^[A-Z_]*$', 'Le texte doit être en majuscule.')],)

    def register(self):
        self.save()

    def __str__(self):
        return self.type


class Announcement(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.ForeignKey(AnnouncementType, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.message
