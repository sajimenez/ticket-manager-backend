from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('OPEN', _('Open')),
        ('PENDING', _('Pending')),
        ('IN_PROGRESS', _('In progress')),
        ('SOLVED', _('Solved')),
        ('CLOSED', _('Closed')),
    ]
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    status = models.CharField(_('status'), max_length=50, choices=STATUS_CHOICES)
    created = models.DateTimeField(_('created'), default=timezone.now)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name=_('creator'))

    def __str__(self):
        return self.title
