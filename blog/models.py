from django.db import models
from django.utils.text import slugify
from user.models import BlogUser


# Create your models here.
def up(instance, file):
    _, ext = file.split('.')
    return f"posts/{instance.title}.{ext}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=up, null=False)
    short_desc = models.CharField(max_length=500)
    main_desc = models.TextField()
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.title} by {self.author.nickname}"
