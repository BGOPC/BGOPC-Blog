from django.contrib import admin
from .models import BlogUser

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields= ('id')

admin.site.register(BlogUser)