#-*- coding:utf-8 -*-
from django.http import HttpResponse,JsonResponse
from sign.models import Event,Guest
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError
def add_event(request):
    eid = request.POST.get('eid', '')  # 发布会 id
    name = request.POST.get('name', '')  # 发布会标题
    linit = request.POST.get('linit', '')  # 限制人数
    status = request.POST.get('status', '')  # 状态
    address = request.POST.get('address', '')  # 地址
    start_time = request.POST.get('start_time', '')
    print "eid",eid
    if eid=='' or name=='' or linit=='' or status=='' or address=='' or start_time=='':
        return JsonResponse({"status_code":201,"message":"字段不能为空"})
    result=Event.objects.filter(id=eid)
    if result:
        return JsonResponse({"status_code": 202, "message": "id已经存在了"})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({"status_code": 203, "message": "发布会名称已经存在了"})
    try:
        Event.objects.create(id=eid,name=name,linit=linit,status=int(status),address=address,start_time=start_time)
    except ValidationError:
        return JsonResponse({"status_code": 204, "message": "It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."})
    return JsonResponse({"status_code": 200, "message": "发布会添加成功"})
def query_event(request):
    if request.method=='GET':
        events=Event.objects.all()
        event_lists=[]
        for event in events:
            eventdict={}
            eventdict['name']=event.name
            eventdict['linit']=event.linit
            event_lists.append(eventdict)
        return JsonResponse({"status_code": 200, "message": "查询成功","data":event_lists})
    else:
        return JsonResponse({"status_code": 201, "message": "query method error"})

import  time
# 添加嘉宾接口
def add_guest(request):
    eid = request.POST.get('eid', '')  # 关联发布会 id
    realname = request.POST.get('realname', '')  # 姓名
    phone = request.POST.get('phone', '')  # 手机号
    email = request.POST.get('email', '')  # 邮箱
    if eid == '' or realname == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023,
                             'message': 'event status is not available'})
    event_limit = Event.objects.get(id=eid).linit  # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数
    if len(guest_limit) >= event_limit:
        return JsonResponse({'status': 10024, 'message': 'event number is full'})
    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    print 'event_time',str(event_time).split('+')[0]
    nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print 'nowtime',nowtime
    if str(nowtime)>str(event_time).split('+')[0]:
        return JsonResponse({'status': 10025, 'message': 'event has started'})
    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email,
                             sign=0, event_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status': 10026,
                             'message': 'the event guest phone number repeat'})
    return JsonResponse({'status': 200, 'message': 'add guest success'})

#
# 嘉宾查询接口
def get_guest_list(request):
    eid = request.GET.get("eid", "") # 关联发布会 id
    phone = request.GET.get("phone", "") # 嘉宾手机号
    if eid == '':
        return JsonResponse({'status':10021,'message':'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status':200, 'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022, 'message':'query result is empty'})
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone,event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query result is empty1'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status':200, 'message':'success', 'data':guest})
# 嘉宾签到接口

def user_sign(request):
    print "fef"
    eid = request.POST.get('eid','') # 发布会 id
    phone = request.POST.get('phone','') # 嘉宾手机号
    if eid =='' or phone == '':
        return JsonResponse({'status':10021,'message':'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status':10022,'message':'event id null'})
    result = Event.objects.get(id = eid).status
    if not result:
        return JsonResponse({'status':10023,'message':'event status is not available'})
    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    print 'event_time', str(event_time).split('+')[0]
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print 'nowtime', nowtime
    if str(nowtime) < str(event_time).split('+')[0]:
        return JsonResponse({'status': 10025, 'message': 'event has started'})
    result = Guest.objects.filter(phone = phone)
    if not result:
        return JsonResponse({'status':10025,'message':'user phone null'})
    result = Guest.objects.filter(event_id=eid,phone=phone)
    if not result:
        return JsonResponse({'status':10026,
    'message':'user did not participate in the conference'})
    result = Guest.objects.get(event_id=eid,phone = phone).sign
    if result:
        return JsonResponse({'status':10027,'message':'user has sign in'})
    else:
        Guest.objects.filter(event_id=eid,phone=phone).update(sign='1')
        return JsonResponse({'status':200,'message':'sign success'})

import requests


