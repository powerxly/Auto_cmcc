#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com
import pymysql

connect = pymysql.Connect(
    host='192.168.1.124',
    port=3306,
    user='root',
    passwd='16899168',
    db='test_elements',
    charset='utf8'
)

cursor = connect.cursor()

#插入数据

sqlcreate = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sqlcreate)
connect.commit()
# sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
# data = ('雷军', '13512345678', 10000)
# cursor.execute(sql % data)
# connect.commit()
print('成功插入', cursor.rowcount, '条数据')