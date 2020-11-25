from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must enter their first name")
        if not last_name:
            raise ValueError("Users must enter their last name")

        user = self.model(
               email      = self.normalize_email(email),
               first_name = first_name,
               last_name  = last_name,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):

        user = self.model(
               email      = self.normalize_email(email),
               first_name = first_name,
               last_name  = last_name,
               password   = password,
            )

        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True

        user.save(using=self._db)
        return user



class Users(AbstractBaseUser, PermissionsMixin):
    email        = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined  = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active    = models.BooleanField(default=True)   ## Everything within these comment tags
    is_admin     = models.BooleanField(default=False)  ## define the permissions
    is_staff     = models.BooleanField(default=False)  ## that the user will have unless
    is_superuser = models.BooleanField(default=False)  ## changed by the superuser/admin.
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email + "," + self.first_name + "" + self.last_name # Returns the email, first name and
                                                                        # last name of the user in CMD.

    def has_perm(self, perm, obj=None): # Assigns the permissions that the user has
        return "Admin:" + " " + self.is_admin

    def has_module_perms(self, app_label):
        return True
