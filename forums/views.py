from django.shortcuts import render, redirect
from .models import Forum,Events,Notices,JoinReq
from chat.models import Room
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
from .forms import ScheduleForm, NoticeForm, ForumForm
from users.models import CustomUser
# Create your views here.

def forum(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    members = forum.users.all()
    if request.user in members:
        if request.method == 'POST':
            if "chat" in request.POST:
                room = Forum.objects.get(id=forum_id)
                roomName = room.name
                user = request.user.first_name
                if Room.objects.filter(name=roomName).exists():
                    return redirect('/chat/' + roomName + '/?user=' + user)
                else:
                    newRoom = Room.objects.create(name=roomName)
                    newRoom.save()
                    return redirect('/chat/' + roomName + '/?user=' + user)
            elif "notice" in request.POST:
                noticeform = NoticeForm(request.POST)
                if noticeform.is_valid():
                    noticeform.save()
                    return redirect('/forums/'+forum_id)                
            else:
                form = ScheduleForm(request.POST)
                if form.is_valid():
                    event = form.save()
                    event1 = Events.objects.get(id=event.id)
                    event1.users_added.add(request.user)
                    return redirect('/forums/'+forum_id)
                else:
                    return HttpResponse(f'Form error: {form.errors}')
        else:
            events = Events.objects.filter(forum__id = forum_id).order_by('date').filter(Q(date__gte=timezone.now()))
            notices = Notices.objects.filter(forum__id=forum_id)
            form = ScheduleForm()
            noticeform = NoticeForm()            
            mods = forum.mods.all()
            context = {'forum':forum,'events':events,'notices':notices,'form':form,'noticeform':noticeform,'members':members,'mods':mods}
            return render(request,'forum.html',context)
    else:
        member = CustomUser.objects.get(reg_no=request.user)
        forum = Forum.objects.get(id=forum_id)
        if request.method == "POST":
            if "request" in request.POST:
                req = JoinReq.objects.filter(forum=forum,user=member)
                if not req:
                    JoinReq.objects.create(forum=forum,user=member)
        req = JoinReq.objects.filter(forum=forum,user=member)
        context = {'req':req}
        return render(request,'request.html',context)
        
        

def test(request):
    return render(request, 'test.html')

def event(request,event_id):
    if request.method=='POST':
        if 'addevent' in request.POST:
            event = Events.objects.get(id=event_id)
            event.users_added.add(request.user)
            context = {'event':event,'forum':forum}
            return render(request,'event.html',context)
        elif 'removeevent' in request.POST:
            event = Events.objects.get(id=event_id)
            event.users_added.remove(request.user)
            context = {'event':event,'forum':forum}
            return render(request,'event.html',context)       
        else:
            room = Events.objects.get(id=event_id)
            roomName = room.title
            user = request.user.first_name
            if Room.objects.filter(name=roomName).exists():
                return redirect('/chat/' + roomName + '/?user=' + user)
            else:
                newRoom = Room.objects.create(name=roomName)
                newRoom.save()
                return redirect('/chat/' + roomName + '/?user=' + user)
    else:    
        event = Events.objects.get(id=event_id)
        context = {'event':event,'forum':forum}
        return render(request,'event.html',context)

'''
def member_list(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    user_forums = request.user.forums.all()
    if forum.is_public or forum in user_forums:
        members = forum.users.all()
        mods = forum.mods.all()
        context = {'members':members,'mods':mods}
        return render(request,'members.html',context)
    else:
        valid = False
        context = {'valid':valid}
        return render(request,'invalid.html',context)
''' 
       
''' if request.method == 'POST':
        if request.POST.get('chat')==True:
            room = Forum.objects.get(id=forum_id)
            roomName = room.name
            user = request.user.first_name
            if Room.objects.filter(name=roomName).exists():
                return redirect('/chat/' + roomName + '/?user=' + user)
            else:
                newRoom = Room.objects.create(name=roomName)
                newRoom.save()
                return redirect('/chat/' + roomName + '/?user=' + user)
        else:
            form = ScheduleForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('success')'''
                

def member_list(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    if request.user in forum.mods.all():
        if request.method == 'POST' :
            if 'accept' in request.POST:
                member = CustomUser.objects.get(reg_no=request.POST['accept'])
                forum.users.add(member)
                JoinReq.objects.filter(forum=forum,user=member).delete()
            elif 'remove' in request.POST:
                member = CustomUser.objects.get(reg_no=request.POST['remove'])
                if member in forum.mods.all():
                    forum.mods.remove(member)
                forum.users.remove(member)
            elif 'makemod' in request.POST:
                member = CustomUser.objects.get(reg_no=request.POST['makemod'])
                forum.mods.add(member)
            elif 'removemod' in request.POST:
                member = CustomUser.objects.get(reg_no=request.POST['removemod'])
                forum.mods.remove(member)               
        else:
            pass
        mods = forum.mods.all()
        members = forum.users.all()
        join_reqs = JoinReq.objects.filter(forum = forum)
        context = {'join_reqs':join_reqs,'members':members,'mods':mods}
        return render(request,'members.html',context)
    else:
        return render(request,'test.html')


def makeforum(request):
    if request.user.is_staff:
        if request.method == 'POST':
            forumform = ForumForm(request.POST)
            if forumform.is_valid():
                forumform1 = forumform.save()
                forumform2 = Forum.objects.get(id = forumform1.id)
                forumform2.users.add(request.user)
                forumform2.mods.add(request.user)
                print ('success')
                context={'forumform':forumform}
                return render(request,'makeforum.html',context)
        else:
            forumform = ForumForm()
            context={'forumform':forumform}
            return render(request,'makeforum.html',context)
