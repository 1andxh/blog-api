from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content  = models.TextField()
    tag = TaggableManager(verbose_name="Tags",blank=True)
    category = models.CharField(max_length=30, default="uncategorized")
    draft = models.BooleanField(default=False)
    published = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title.capitalize