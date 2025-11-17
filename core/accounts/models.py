from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .validators import validate_iranian_cellphone_number
from django.core.validators import RegexValidator

# Create your models here.
class UserType(models.IntegerChoices):
    customer = 1 , _("customer")
    admin = 2 , _("admin")
    superuser = 3 , _("superuser")

class UserManager(BaseUserManager):
    """
    custom user model manager where email is the unique identifiers for authentication
    instead of username
    """
    def create_user(self, email, password, **extra_fields):
        """
        create and save user
        """
        if not email:
            raise ValueError(_("the Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        create and save superuser
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("type", UserType.superuser.value)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("superuser must have is is_staff= true"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser= true"))
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("emial address"), unique= True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=UserType.choices, default=UserType.customer.value)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, validators=[validate_iranian_cellphone_number])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and instance.type == UserType.customer.value:
        Profile.objects.create(user= instance)