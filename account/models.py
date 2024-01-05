import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from account.managers import UserManager

from django.templatetags.static import static


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    avatar = models.FileField(_('Avatar'), default=None, null=True, blank=True, upload_to='avatars/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def avatar_url(self) -> str:
        if self.avatar:
            return self.avatar.url

        return static('red_cat.jpg')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()

        return super().save(*args, **kwargs)
