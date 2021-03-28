from django.db import models
from django.core.exceptions import ValidationError
import re

def validateEmail(value):
	email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	if not email_regex.match(value):
		raise ValidationError("Invalid email address".format(value))
	elif len(User.objects.filter(email=value)) > 0:
		raise ValidationError("Email already registered".format(value))

def validatePassword(value):
	if len(value) < 8:
		raise ValidationError("Password must be at least 8 characters".format(value))

def validateUsername(value):
	if len(User.objects.filter(username=value)) > 0:
		raise ValidationError("Username already taken".format(value))

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	style = models.CharField(max_length=255, blank=True, null=True)
	cityState = models.CharField(max_length=255)
	phone = models.CharField(max_length=20, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	chefs = models.ForeignKey(Restaurant, related_name="chefs", on_delete=models.PROTECT, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
	title = models.CharField(max_length=255)
	uploader = models.ForeignKey(User, related_name='userPictures', on_delete=models.PROTECT, blank=True, null=True)
	restaurant = models.ForeignKey(Restaurant, related_name='restaurantPictures', on_delete=models.PROTECT, blank=True, null=True)
	restaurantProfilePic = models.ForeignKey(Restaurant, related_name="restaurantProfilePic", on_delete=models.PROTECT, blank=True, null=True)
	content = models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


