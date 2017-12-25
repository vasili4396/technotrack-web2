from django.db import models


class Category(models.Model):
    name = models.CharField(default='', max_length=255)
    createdata = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name
