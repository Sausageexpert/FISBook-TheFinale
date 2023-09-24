from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'homeStuff.html')

def checkForRoom(request):
    room = request.POST['roomName']
    user = request.POST['user']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?user=' + user)
    else:
        newRoom = Room.objects.create(name=room)
        newRoom.save()
        return redirect('/' + room + '/?user=' + user)
        
def room(request, room):
    user=request.GET.get('user')
    msgs = Message.objects.filter(room=room)
    return render(request, 'roomStuff.html', context={'room':room, 'user':user, 'msgs':msgs})

def send(request):
    user=request.POST.get('user')
    value=request.POST.get('value')
    room=request.POST.get('room')
    newMsg = Message.objects.create(user=user, value=value, room=room)
    newMsg.save()
    return HttpResponse('sent')

def get(request, room):
    messages = Message.objects.filter(room=room)
    messagesData=[]
    for message in messages:
        messagesData.append({'user':message.user, 'value':message.value, 'date':message.date})
    return JsonResponse({'messages': messagesData})