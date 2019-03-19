#-*- coding:utf-8 -*-
import sys
#sys.path.append('../dbfix')
print sys.path
from mysql_db import DB
datas1 = {
'sign_event':[
{'id':1,'name':'红米 Pro 发布会','linit':2000,'status':1,
'address':'北京会展中心','start_time':'2017-08-20 14:00:00','create_time':'2019-02-21 08:56:39'},
{'id':2,'name':'可参加人数为 0','linit':0,'status':1,
'address':'北京会展中心','start_time':'2017-08-20 14:00:00','create_time':'2019-02-21 08:56:39'},
{'id':3,'name':'当前状态为 0 关闭','linit':2000,'status':0,
'address':'北京会展中心','start_time':'2017-08-20 14:00:00','create_time':'2019-02-21 08:56:39'},
{'id':4,'name':'发布会已结束','linit':2000,'status':1,
'address':'北京会展中心','start_time':'2001-08-20 14:00:00','create_time':'2019-02-21 08:56:39'},
{'id':5,'name':'小米 5 发布会','linit':2000,'status':1,
'address':'北京国家会议中心','start_time':'2017-08-20 14:00:00','create_time':'2019-02-21 08:56:39'},
],'sign_guest':[
{'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com',
'sign':0,'event_id':1,'create_time':'2019-02-21 08:56:39'},
{'id':2,'realname':'has ign','phone':13511001101,'email':'sign@mail.com',
'sign':1,'event_id':1,'create_time':'2019-02-21 08:56:39'},
{'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com',
'sign':0,'event_id':5,'create_time':'2019-02-21 08:56:39'},
]
}
def init_data():
    for tablename,datas in datas1.items():
        DB().clear_data(str(tablename))
        for data in datas:
            DB().insert_data(str(tablename), data)
if __name__ == '__main__':
    init_data()