from tabnanny import verbose
from django.db import models
from modules.categories.models import *
from modules.users.models import *
from modules.locations.models import *

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"    
    heading = models.CharField(verbose_name=("Post heading"), max_length=100)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description')
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=False, blank=False, on_delete=models.CASCADE)
    mobile = models.CharField(verbose_name=("Mobile Number"), max_length=13, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.heading)

class PostAssets(models.Model):
    class Meta:
        verbose_name = "Post Asset"
        verbose_name_plural = "Post Assets"
    post = models.ForeignKey(Post,null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.post)