from __future__ import unicode_literals

from django.db import models
from firebasetoken.utils import *
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from firebasetoken.utils import *

# Create your models here.
class FirebaseToken(models.Model):

    key = models.CharField(_("Key"), max_length=1500, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='firebasetoken',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("FirebaseToken")
        verbose_name_plural = _("FirebaseToken")

    def save(self, *args, **kwargs):
        if self.user and not self.key:
            self.key = self.generate_key(self.user)
        return super(FirebaseToken, self).save(*args, **kwargs)

    def generate_key(self, user):
        return create_firebase_token(user)


    def __str__(self):
        return self.key
