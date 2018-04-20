from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, AbstractUser
from Core.models import ShowMixin, EventMixin
from Like.models import LikeMixin
from Post.models import Post
from Comment.models import CommentMixin
from datetime import datetime
from django.utils import six
from django.contrib.auth.validators import ASCIIUsernameValidator, UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    gender_choices = (
                        ('M', 'male'),
                        ('F', 'female'),
                    )
    sex = models.CharField(null=True, blank=True, max_length=1, choices=gender_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

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

    def get_posts(self):
        return Post.objects.filter(author_id=self.id)


class Avatar(LikeMixin, CommentMixin, ShowMixin, EventMixin):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    user = models.ForeignKey(CustomUser, related_name='avatar')

    class Meta:
        unique_together = ('avatar', 'user')

    def get_author(self):
        return self.user

    def get_title(self):
        return "%s now has new avatar %s" % (self.get_author(), self.avatar)

