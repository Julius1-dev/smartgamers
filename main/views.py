from django.shortcuts import render
from .models import Room
from .forms import RoomForm
from django.contrib import messages

def home(request):
    rooms= Room.objects.all()
    context= {'rooms':rooms}
    return render(request, 'main/home.html',context)

def room(request,pk):    
    room=Room.objects.all()
    context={'room':room}    
    return render(request, 'main/room.html',context)

def addRoom(request):
    form=RoomForm()
    if request.method=="POST":
        form=RoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Room Successfully added!")
        
        else:
            for error in list(form.errors.values()):
                 messages.error(request, error)
    else:
        form=RoomForm()
    return render(request=request,
                  template_name="main/addroom.html",
                  context={'form':form}
                )
            



