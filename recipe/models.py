from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, reg_id, privilege, password=None):
        """
        Creates and saves a user with the given serial number.
        """
        user = self.model(
            reg_id=reg_id,
            privilege=privilege,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, reg_id, password=None):
        """
        Creates and saves a superuser with the given serial number, password.
        """
        user = self.model(
            reg_id=reg_id,
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    reg_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default="", blank=True, null=True)
    email_is_verify = models.BooleanField(default=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(blank=True, null=True)
    privilege = models.PositiveSmallIntegerField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'reg_id'

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name


class Cookbook(models.Model):
    name = models.CharField(max_length=20)
    c_image = models.FileField(upload_to='cookbook/')
    for_people_num = models.SmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)
    like = models.PositiveSmallIntegerField(default=0)
    click_freq = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('User', on_delete=models.PROTECT, related_name='cookbook_created')
    is_valid = models.BooleanField(default=False)

    STATES_CHOICES = (
        (0, '儲存'),
        (1, '發布'),
    )
    state = models.SmallIntegerField(choices=STATES_CHOICES, default=0)

    def __str__(self):
        return self.name


class Group(models.Model):
    cookbook = models.ForeignKey('Cookbook', on_delete=models.PROTECT)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    group = models.ForeignKey('Group', on_delete=models.PROTECT, blank=True)
    cookbook = models.ForeignKey('Cookbook', on_delete=models.PROTECT)
    name = models.CharField(max_length=15)
    quantity = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Step(models.Model):
    cookbook = models.ForeignKey('Cookbook', on_delete=models.PROTECT)
    s_image = models.FileField(upload_to='step/', blank=True, null=True)
    description = models.TextField(max_length=150)
    tips = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.description


class MessageBoard(models.Model):
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='message_created')
    image = models.FileField(upload_to='comment', blank=True, null=True)
    message = models.TextField(max_length=400)

