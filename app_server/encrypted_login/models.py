from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class AuthChecker(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    q_code = models.CharField(max_length=6)
    status = models.CharField(max_length=15, default="wait")
    created_date = models.DateTimeField(blank=True, editable=False, default=timezone.now)
    expired_date = models.DateTimeField()

    def __str__(self):
        return "%s_%s" % (self.user, self.q_code)

    def save(self, *args, **kwargs):
        """ On save """
        if not self.id:
            # For session time (2 minutes)
            self.created_date = timezone.now()
            self.expired_date = (self.created_date + timezone.timedelta(seconds=120))
        return super(AuthChecker, self).save(*args, **kwargs) 
    
    def is_expired(self):
        if timezone.now() > self.expired_date:
            return True
        else:
            return False
