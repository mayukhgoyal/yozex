from tabnanny import verbose
from django.db import models
from modules.users.models import *

# Create your models here.
class Feedbacks(models.Model):
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
    
    subject = models.CharField(verbose_name=("Subject"), max_length=100)
    message = models.TextField()
    user = models.ForeignKey(User, null=False, blank=False,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.subject)