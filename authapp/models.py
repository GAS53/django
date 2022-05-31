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


class CustomAccountManager(BaseUserManager):

    def create_user(self, position, email, user_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('Email должен быть для создания пользователя'))
        elif not password:
            raise ValueError(_('необходимо задать пароль'))
        elif not user_name:
            raise ValueError(_('невозможно создать пользователя без имени'))

        if position == 'staff':
            other_fields.setdefault('is_staff', True)
            position = 'админ без доступа к новостям'
        elif position == 'superuser':
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_superuser', True)
            position = 'суперпользователь'
        elif position == 'news_manadjer':
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_news_manadjer', True)
            position = 'менеджер новостей'
        else:
            position = 'обычный пользователь'
        messages.add_message(self.request, messages.INFO, _(f"создан {position} \n{self.request.user.get_full_name()}"))

        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()

        return self.create_user(email, user_name, password, **other_fields)






class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    user_name = models.CharField(max_length=150, unique=True, help_text=_("Не больше 150 символов"),
        validators=[username_validator], error_messages={ "unique": _("Пользователь с таким ником уже существует"),},)
    first_name = models.CharField(_('Имя'), max_length=150, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=20, blank=True)
    avatar = models.FileField(verbose_name='аватарка')
    age = models.SmallIntegerField(verbose_name='Возраст')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_news_manadjer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)   

    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()
    

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


