from django.shortcuts import render
from .models import Room

def home(request):
    rooms= Room.objects.all()
    context= {'rooms':rooms}
    return render(request, 'main/home.html',context)

def room(request,pk):    
    room=Room.objects.all()
    context={'room':room}    
    return render(request, 'main/room.html',context)


