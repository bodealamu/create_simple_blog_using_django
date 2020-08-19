from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, PermissionsMixin

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        """
        Function for creating a user
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('Users must have an email')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')

        # superman@GMAIL.COM or superman@gMail.com

        user = self.model(
            email= self.normalize_email(email=email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates a super user
        :param email:
        :param first_name:
        :param last_name:
        :param password:
        :return:
        """
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Model representation for a User"""
    first_name = models.CharField(max_length=20, verbose_name='What is your first name')
    last_name = models.CharField(max_length=20, verbose_name='What is your last name')
    email = models.EmailField(max_length=40, verbose_name='What is your email address?', unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name','last_name']

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        first = self.first_name
        last = self.last_name
        fullname = str(first) + ' ' + str(last)

        return fullname
