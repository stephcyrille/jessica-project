from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class AuthChecker(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    q_code = models.CharField(max_length=6)
    status = models.CharField(max_length=15, default="wait")
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)