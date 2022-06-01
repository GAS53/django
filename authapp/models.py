from pathlib import Path
from time import time
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


def users_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f"user_{instance.user_name}/avatars/pic_{num}{suff}"

class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None):
        if not user_name:
            raise ValueError('Должно быть задано имя пользователя')

        user = self.model(user_name=user_name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, password=None):
        user = self.create_user(
            user_name,
            password=password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user






class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    user_name = models.CharField(_("user_name"), max_length=150, unique=True, help_text=_("Не больше 150 символов"),
        validators=[username_validator], error_messages={ "unique": _("Пользователь с таким ником уже существует"),},)
    first_name = models.CharField(_("first_name"), max_length=150, blank=True)
    last_name = models.CharField(_("last_name"), max_length=150, blank=True)
    email = models.EmailField(_('email'), blank=True)
    mobile = models.CharField(_("mobile"), max_length=20, blank=True)
    age = models.SmallIntegerField(_("age"), blank=True, null=True)
    avatar = models.FileField(_("avatar"), blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_news_manadjer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)   

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD = 'user_name'

    objects = UserManager()
    

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()
        
    def get_short_name(self):
        return self.first_name

    def send_email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.user_name
