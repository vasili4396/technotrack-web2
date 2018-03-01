from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from Core.models import ShowMixin
from Like.models import LikeMixin
from Comment.models import CommentMixin


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, is_admin, password):

        user = self.model(
            email=email,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def get_by_natural_key(self, email_):
    #     return self.get(email=email_)


class CustomUser(AbstractBaseUser):
    gender_choices = (
                        ('M', 'male'),
                        ('F', 'female'),
                    )

    email = models.EmailField(max_length=127, unique=True, blank=False, null=False)
    first_name = models.CharField(null=True, max_length=255, blank=False)
    last_name = models.CharField(null=True, max_length=255, blank=False)
    sex = models.CharField(null=True, blank=True, max_length=1, choices=gender_choices)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['is_admin']

    class Meta:
        app_label = "User"

    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Avatar(LikeMixin, CommentMixin, ShowMixin):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    user = models.OneToOneField('User.CustomUser')

    def get_author(self):
        return "%s " % self.user.first_name

