from django.shortcuts import render, redirect
from .models import *
from .forms import placesForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    places = Places.objects.all()
    return render(request, "travelapp/home.html", {'place':places})
def detail(request, id):
    indvPlace = Places.objects.get(id=id)
    return render(request, 'travelapp/detail.html', {'indvPlace':indvPlace})

def aboutjs(request):
    return render(request, 'travelapp/js.html',{})


def addplaces(request):
    form = placesForm()
    if request.method == "POST":
        form = placesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        print(form.errors)
    form = placesForm()
    return render(request, "travelapp/placeform.html",{'form':form})


def updatePlace(request, pk):
    places = Places.objects.get(id=pk)
    placeForm = placesForm(instance=places)
    if request.method == "POST":
        placeForm = placesForm(request.POST,request.FILES ,instance=places)
        if placeForm.is_valid():
            placeForm.save()
            return redirect("home")
        print(placeForm.errors)
        return HttpResponse("Error Occured")  
    return render(request, "travelapp/placeform.html",{'form':placeForm})


def deletePlace(request, pk):
    places = Places.objects.get(id=pk)
    places.delete()
    return redirect("home")
    return render(request, "travelapp/placeform.html",{})
