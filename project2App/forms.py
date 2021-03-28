from django.db import models
from django import forms
import re
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.core.exceptions import ValidationError
import bcrypt
from project2App.models import *

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']

class RawUserLoginForm(forms.Form):
	email = forms.CharField(max_length=255)
	password = forms.CharField(max_length=255, validators=[validatePassword])

	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")
		user = User.objects.filter(email=email)
		if len(user) < 1:
			raise ValidationError("User does not exist".format())
		hashedPassword = user[0].password
		if bcrypt.checkpw(password.encode(), hashedPassword.encode()) == False:
			raise ValidationError("Incorrect password".format())

		return super(RawUserLoginForm, self).clean()

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password']

class RawUserRegisterForm(forms.Form):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	username = forms.CharField(max_length=255, validators=[validateUsername])
	email = forms.CharField(max_length=255, validators=[validateEmail])
	password = forms.CharField(max_length=255, validators=[validatePassword])

	def clean(self, *args, **kwargs):
		first_name = forms.CharField(max_length=255)
		last_name = forms.CharField(max_length=255)
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		return super(RawUserRegisterForm, self).clean()

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['title', 'content']

class RawImageUploadForm(forms.Form):
	title = forms.CharField(max_length=255)
	content = forms.ImageField()

	def clean(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		content = self.cleaned_data.get('content')
		return super(RawImageUploadForm, self).clean()

class RestaurantCreateForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'address', 'style', 'cityState']

class RawRestaurantCreateForm(forms.Form):
	name = forms.CharField(max_length=255)
	address = forms.CharField(max_length=255)
	style = forms.CharField(max_length=255, required=False)
	cityState = forms.CharField(max_length=255, label="City, State")

	def clean(self, *args, **kwargs):
		name = self.cleaned_data.get('title')
		address = self.cleaned_data.get('address')
		style = self.cleaned_data.get('style')
		cityState = self.cleaned_data.get('cityState')
		return super(RawRestaurantCreateForm, self).clean()

# class AddChef(forms.ModelForm):
# 	class Meta:
# 		model = Restaurant
# 		fields = ['chefs']

# class RawAddChef(forms.Form):
# 	allUsersList = []
# 	allUsers = User.objects.all()
# 	for user in allUsers:
# 		allUsersList.append(user)
# 	chefs = forms.MultipleChoiceField(choices=allUsersList)

