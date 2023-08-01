from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home/<int:id>/', views.detail, name="detail"),
    path('aboutjs/', views.aboutjs, name="aboutjs"),
    path('addplaces/', views.addplaces, name="addplaces"),
    path('update-places/<int:pk>/', views.updatePlace, name="updatePlaces"),
    path('delete-place/<int:pk>/', views.deletePlace,name="deletePlace")
]
