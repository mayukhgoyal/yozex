from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    category_name = models.CharField(verbose_name=("Category Name"), max_length=100)
    category_image = models.ImageField(blank=True, null=True, upload_to='category-image')
    parent_category = models.ForeignKey('self', null=True,blank=True, related_name='children',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category_name)

