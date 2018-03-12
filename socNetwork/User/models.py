from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, AbstractUser
from Core.models import ShowMixin, EventMixin
from Like.models import LikeMixin
from Comment.models import CommentMixin
from datetime import datetime


# # TODO: BaseUser
# class CustomUserManager(BaseUserManager):
#     def create_superuser(self, email, is_admin, password):
#
#         user = self.model(
#             email=email,
#             is_admin=is_admin
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username=None, email=None, password=None):
#         now = datetime.now()
#         if email is None:
#             raise ValueError('The given email must be set')
#         email = UserManager.normalize_email(email)
#         user = self.model(email=email,
#                           is_admin=False,
#                           )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     # def get_by_natural_key(self, email_):
#     #     return self.get(email=email_)


class CustomUser(AbstractUser):
    gender_choices = (
                        ('M', 'male'),
                        ('F', 'female'),
                    )
    sex = models.CharField(null=True, blank=True, max_length=1, choices=gender_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    email = models.EmailField('email_address', unique=True, blank=False)
    REQUIRED_FIELDS = []

    class Meta:
        app_label = "User"

    def clean(self):
        super(AbstractUser, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Avatar(LikeMixin, CommentMixin, ShowMixin, EventMixin):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    user = models.OneToOneField('User.CustomUser', on_delete=models.CASCADE)

    def get_author(self):
        return self.user

    def get_title(self):
        return "%s now has new avatar %s" % (self.get_author(), self.avatar)

