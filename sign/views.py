# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def hello(request):
    return  render(request,'index.html')
def login_action(request):
    if request.method=='POST': #请求处理的
        username=request.POST.get('username','')
        password=request.POST.get("password",'')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = username
            respone= HttpResponseRedirect("/event_manage/") #这种重定向的路径为http://127.0.0.1:8000/event_manage/
            #HttpResponseRedirect("event_manage")这种重定向的路径为http://127.0.0.1:8000/login_action/event_manage/
            #respone.set_cookie('user',username,3600)
            return respone
        else:
            return render(request,'index.html',{'error':"error username or password"})
@login_required
def event_manage(request):
    #username=request.COOKIES.get("user",'')
    events=Event.objects.all()
    username=request.session.get('user','')
    return  render(request,'event_manage.html',{'username':username,'events':events})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    name=request.GET.get('name')
    events=Event.objects.filter(name__contains=name)
    return render(request, 'event_manage.html', {'username': username, 'events': events})

def guest_manage(request):
    guests = Guest.objects.all()
    username = request.session.get('user', '')
    paginator=Paginator(guests,3)
    print 'paginator.num_pages',paginator.num_pages
    page=request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'guest_manage.html', {'username': username, 'guests': contacts})

def guest_search_name(request):
    username = request.session.get('user', '')
    name=request.GET.get('name')

    guests=Guest.objects.filter(realname__contains=name) #模糊查询
    return render(request, 'guest_manage.html', {'username': username, 'guests': guests})

def sign_index(request,event_id):
    event=get_object_or_404(Event,id=event_id)  #id不存在的时候返回404的页面  不会直接返回一个异常的页面的
    print event,event.name
    return render(request,'sign_index.html',{'event':event})
def sign_index_action(request,event_id):
    phone=request.POST.get('phone')
    result=Guest.objects.filter(phone=phone)
    signnum=0
    guests=Guest.objects.filter(event_id=event_id)
    for guest in guests:
        if guest.sign==1:
            signnum+=1
    print 'signnum',signnum
    totalnum=len(Guest.objects.filter(event_id=event_id)) #总嘉宾数查询
    if not result:
        return render(request,'sign_index.html',{"hit":"phone not exist","totalnum":totalnum,'signnum':signnum})
    result=Guest.objects.filter(phone=phone,event_id=event_id)
    if not result:
        return render(request,'sign_index.html',{"hit":"用户未参加此活动","totalnum":totalnum,'signnum':signnum})
    else:
        sign_status=Guest.objects.get(phone=phone,event_id=event_id).sign #查询的东西
        if sign_status:
            return render(request, 'sign_index.html', {"hit": "用户已签到","totalnum":totalnum,'signnum':signnum})
        else:
            Guest.objects.filter(phone=phone, event_id=event_id).update(sign=1)
            signnum+=1
            return render(request, 'sign_index.html', {"hit": "用户签到成功","totalnum":totalnum,'signnum':signnum})
def logout(request):
    return render(request,'index.html')


