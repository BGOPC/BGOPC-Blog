from django.db import models
# Create your models here.

class BlogUser(models.Model):
    name = models.CharField(max_length=255, null=False)
    nickname = models.CharField(max_length=255, null=True, unique=True)
    join = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="files/profile/", null=True)

    def __str__(self):
        return f"{self.name}: {self.nickname}"