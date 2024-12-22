from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    class Meta:
        proxy = True

    def get_last_name(self):
        return self.last_name


class AgeUser(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}----{self.age}'
