from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.welcome),
	path('register', views.registerPage),
	path('home', views.home),
	path('uploadImagePage', views.uploadImagePage),
	path('viewImagePage/<int:imageID>', views.viewImagePage),
	path('restaurantPage', views.restaurantMain),
	path('createRestaurant', views.restaurantForm),
	path('viewRestaurant/<int:restaurantID>', views.viewRestaurant),
	path('uploadRestaurantPicture/<int:restaurantID>', views.uploadRestaurantPicture),
	path('userPage/<int:userID>', views.userPage),
	path('addChef/<int:restaurantID>', views.addChef),
	path('addChefToRestaurant', views.addChefToRestaurant),
	path('restaurantProfilePic', views.restaurantProfilePic),
	path('logout', views.logout)
]