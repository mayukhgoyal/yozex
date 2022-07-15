from django.db import models
from datetime import date, time, datetime
from django.utils import timezone
from django.utils.timezone import localtime, now
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class UserProfile(models.Model):
	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"
	user = models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)
	name = models.CharField(verbose_name=("Username"), max_length=100)
	mobile = models.CharField(verbose_name=("Mobile Number"), max_length=13, null=False, blank=False,  unique=True)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		return self.name
	def __unicode__(self):
		return unicode(self.name)


class UserOtp(models.Model):
	otp = models.CharField(max_length=100, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.otp)