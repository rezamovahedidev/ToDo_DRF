from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Priority(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'
    URGENT = 'Urgent', 'Urgent'

class ToDo(models.Model):
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='todos',
        null=True,
        blank=True
    )
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title