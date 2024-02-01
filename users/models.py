from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if not other_fields.get('is_staff'):
            raise ValueError('Superuser must be assigned is_staff=True')

        if not other_fields.get('is_active'):
            raise ValueError('Superuser must be assigned is_active=True')

        if not other_fields.get('is_superuser'):
            raise ValueError('Superuser must be assigned is_superuser=True')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password=None, **other_fields):
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUsers(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    econtact = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    