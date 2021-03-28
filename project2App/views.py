from django.shortcuts import render, redirect, HttpResponse
from project2App.models import *
from project2App.forms import *
import bcrypt

def welcome(request):
	form =	RawUserLoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get('email')
			user = User.objects.get(email=email)
			request.session['loggedInUserID'] = user.id
			return redirect('/home')
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	context = {
		'form':form,
		'backgroundImage':backgroundImage
	}
	return render(request, 'welcomePage.html', context)

def registerPage(request):
	form = RawUserRegisterForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			rawPassword = form.cleaned_data.get('password')
			hashedPassword = bcrypt.hashpw(rawPassword.encode(), bcrypt.gensalt()).decode()
			user = User.objects.create(
					first_name=form.cleaned_data.get('first_name'),
					last_name=form.cleaned_data.get('last_name'),
					username=form.cleaned_data.get('username'),
					email=form.cleaned_data.get('email'),
					password=hashedPassword
				)
			request.session['loggedInUserID'] = user.id
			return redirect('/home')
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	context = {
		'form':form,
		'backgroundImage':backgroundImage
	}
	return render(request, 'registerPage.html', context)

def home(request):
	if 'loggedInUserID' not in request.session:
		return redirect('/')
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	thisUser = User.objects.get(id=request.session['loggedInUserID'])
	images = Image.objects.filter(uploader=thisUser)
	context = {
		'images':images,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'backgroundImage':backgroundImage,
		'profileImage':profileImage
	}
	if request.session['loggedInUserID'] == 8:
		return render(request, 'adminHomePage.html', context)
	else:
		return render(request, 'homePage.html', context)

def uploadImagePage(request):
	if 'loggedInUserID' not in request.session:
		return redirect('/')
	if request.method == 'POST':
		form = RawImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			uploader = User.objects.get(id=request.session['loggedInUserID'])
			image = Image.objects.create(
				title=form.cleaned_data.get('title'),
				uploader=uploader,
				content=form.cleaned_data.get('content')
				)
	else:
		form = RawImageUploadForm(None)
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	context = {
		'backgroundImage':backgroundImage,
		'form' : form,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'profileImage':profileImage
	}
	return render(request, 'uploadImagePage.html', context)

def viewImagePage(request, imageID):
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	image = Image.objects.get(id=imageID)
	context = {
		'backgroundImage':backgroundImage,
		'image':image,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'profileImage':profileImage
	}
	return render(request, 'viewImagePage.html', context)

def restaurantMain(request):
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	restaurants = Restaurant.objects.all()
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	context = {
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'backgroundImage':backgroundImage,
		'restaurants':restaurants,
		'profileImage':profileImage,
	}
	return render(request, 'restaurantMain.html', context)

def restaurantForm(request):
	if request.method == 'POST':
		form = RawRestaurantCreateForm(request.POST)
		if form.is_valid():
			restaurant = Restaurant.objects.create(**form.cleaned_data)
			return redirect(f'/viewRestaurant/{restaurant.id}')
	else:
		form = RawRestaurantCreateForm()
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	context = {
		'form':form,
		'backgroundImage':backgroundImage,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'profileImage':profileImage
	}
	return render(request, 'createRestaurantPage.html', context)

def viewRestaurant(request, restaurantID):
	restaurant = Restaurant.objects.get(id=restaurantID)
	restaurantProfilePicList = restaurant.restaurantProfilePic.all()
	images = [] 
	restaurantImages = Image.objects.filter(restaurant=restaurant)
	for image in restaurantImages:
		images.append(image)
	if len(restaurantProfilePicList) > 0:
		chosenPic = restaurantProfilePicList[0]
	elif len(restaurantImages) != 0:
		chosenPic = images[0]
	else:
		chosenPic = None
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	chefs = restaurant.chefs.all()
	context = {
		'restaurant': restaurant,
		'backgroundImage':backgroundImage,
		'restaurantPictures':images,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'profileImage':profileImage,
		'chefs':chefs,
		'restaurantProfilePic':chosenPic
	}
	return render(request, 'viewRestaurantPage.html', context)

def uploadRestaurantPicture(request, restaurantID):
	if request.method == 'POST':
		form = RawImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			uploader = User.objects.get(id=request.session['loggedInUserID'])
			restaurant = Restaurant.objects.get(id=restaurantID)
			image = Image.objects.create(
				uploader=uploader, 
				restaurant=restaurant,
				title=form.cleaned_data.get('title'),
				content=form.cleaned_data.get('content')
				)
			print('IMAGE CREATED **************')
			print(image.content)
			return redirect(f'/viewRestaurant/{restaurantID}')
	else:
		form = RawImageUploadForm()
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	context = {
		'restaurant': Restaurant.objects.get(id=restaurantID),
		'backgroundImage':backgroundImage,
		'form':form,
		'user':User.objects.get(id=request.session['loggedInUserID']),
		'profileImage':profileImage
	}
	return render(request, 'uploadRestaurantPicturePage.html', context)

def userPage(request, userID):
	reqUser = User.objects.get(id=userID)
	thisUser = User.objects.get(id=request.session['loggedInUserID'])
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	context = {
		'backgroundImage':backgroundImage,
		'reqUser':reqUser,
		'profileImage':profileImage,
		'user':thisUser
	}
	return render(request, 'userPage.html', context)

def addChef(request, restaurantID):
	galleryUser = User.objects.get(username='image_gallery')
	backgroundImage = Image.objects.get(title='homeBackground', uploader=galleryUser)
	profileImage = Image.objects.get(uploader=galleryUser, id=9)
	thisUser = User.objects.get(id=request.session['loggedInUserID'])
	allUsers = User.objects.all()
	thisRestaurant = Restaurant.objects.get(id=restaurantID)
	context = {
		'backgroundImage':backgroundImage,
		'profileImage':profileImage,
		'user':thisUser,
		'allUsers':allUsers,
		'restaurant':thisRestaurant
	}
	return render(request, 'addChefPage.html', context)

def addChefToRestaurant(request):
	print('LOOK HERE ******************')
	print(request.POST)
	restaurantID = request.POST['restaurant']
	restaurant = Restaurant.objects.get(id=restaurantID)
	chefID = request.POST['chefs']
	chef = User.objects.get(id=chefID)
	restaurant.chefs.add(chef)
	return redirect(f'/viewRestaurant/{restaurantID}')

def restaurantProfilePic(request):
	restaurantID = Restaurant.objects.get(id=request.POST['restaurantID']).id
	restaurant = Restaurant.objects.get(id=restaurantID)
	picture = Image.objects.get(title=request.POST['chosenPic'])
	profilePics = restaurant.restaurantProfilePic.all()
	while len(restaurant.restaurantProfilePic.all()) > 0:
		restaurant.restaurantProfilePic.clear()
		#reUpload = Image.objects.create(id=OPid, title=OPtitle, uploader=OPuploader, restaurant=OPrestaurant, content=OPcontent)
	restaurant.restaurantProfilePic.add(picture)
	return redirect(f'/viewRestaurant/{restaurantID}')

def logout(request):
	request.session.clear()
	return redirect('/')