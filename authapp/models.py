from pathlib import Path
from re import T
from time import time
from wsgiref.validate import validator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

def users_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f"user_{instance.username}/avatars/pic_{num}{suff}"

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. ASCII letters and digits only."),
        validators=[username_validator],
        error_messages={ "unique": _("A user with that username already exists."),},)
    first_name = models.CharField(_('Имя'), max_length=150, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    avatar = models.FileField(verbose_name='аватарка')
    age = models.SmallIntegerField(verbose_name='Возраст')

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
        
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []