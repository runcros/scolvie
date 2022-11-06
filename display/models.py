from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class AnnouncementType(models.Model):
    type = models.CharField(max_length=20, validators=[RegexValidator(
        '^[A-Z_]*$', 'Le texte doit être en majuscule.')],)

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

    def __str__(self):
        return self.message


class Teacher(models.Model):
    name = models.CharField(max_length=20)

class Room(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Slot(models.Model):
    name = models.CharField(max_length=2)
    time = models.TimeField()

    def __str__(self):
        return self.name

class Planning(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.name + ' ' + self.room.name + ' ' + self.slot.name