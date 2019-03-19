#-*- coding:utf-8 -*-
import pymysql,ConfigParser,os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\config.ini'
config=ConfigParser.SafeConfigParser()
config.read(path)
host=config.get('mysqlconf','host')
port=config.get('mysqlconf','port')
user=config.get('mysqlconf','user')
password=config.get('mysqlconf','password')
db_name=config.get('mysqlconf','db_name')
class DB():
    def __init__(self):
        self.db = pymysql.connect(host=host, port=int(port), database=db_name, user=user, password=password,
                                  charset='utf8')
        self.cursor=self.db.cursor()
    def clear_data(self,tablename):
        sql1='SET FOREIGN_KEY_CHECKS=0;'
        self.cursor.execute(sql1)
        self.db.commit()
        sql='delete from %s'%tablename
        self.cursor.execute(sql)
        self.db.commit()
    def insert_data(self,table_name,table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        print table_data.keys()
        print table_data.values()
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)
        self.cursor.execute(real_sql)
        self.db.commit()

    def close(self):
        self.db.close()
if __name__=="__main__":
    db=DB()
    db.clear_data('sign_guest')
    db.clear_data('sign_event')
    data={'id':1,'name':'红米 Pro 发布会','linit':2000,'status':1,'address':'北京会展中心','start_time':'2017-08-20 14:00:00','create_time':'2019-02-21 08:56:39'}
    data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com','sign': 0, 'event_id': 1,'id':1,'create_time':'2019-02-21 08:56:39'}
    db.insert_data('sign_event',data)
