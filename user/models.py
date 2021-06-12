from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from behaviors import BaseField


class User(AbstractBaseUser, BaseField):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, blank=True)
    selfie = models.ImageField(upload_to='images/', default='default.png', blank=True, null=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'         # email을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['name']       # 필수입력값

    class Meta:
        verbose_name = 'user'         # 어드민 페이지에서 클래스명 설정(단수)
        verbose_name_plural = 'users' # 어드민 페이지에서 클래스명 설정(복수)
        swappable = 'AUTH_USER_MODEL' # 'AUTH_USER_MODEL'에 의해 변경될 수 있음

    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        pass
        # send_mail(subject, message, from_email, [self.email], **kwargs)