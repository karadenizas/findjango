from PIL import Image 

from django.db import models
from django.contrib.auth.models import (
                                        AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin
                                        )
from django.urls import reverse                                       


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, user_name, password=None):
        
        user = self.create_user(
            email,
            user_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='profile')
    slug = models.SlugField(max_length=50, unique=True)
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile_photos/%Y/%m/')
    about = models.TextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return self.user.user_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('userprofile:user_profile', kwargs={'user': self.slug})
