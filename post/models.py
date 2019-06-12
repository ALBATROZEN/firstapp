from django.db import models

# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=30)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.UserName