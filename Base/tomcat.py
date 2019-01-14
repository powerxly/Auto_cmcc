#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : 洋燚
# @Email   : jasonleeyag@163.com

#coding:utf-8

import os, sys

start_operation = ['startup', '-startup', '--startup', 'start', '-start', '--start']
stop_operation  = ['shutdown', '-shutdown', '--shutdown', 'stop', '-stop', '--stop']
show_operation  = ['show', 'log']
'''
os.system调用系统指令。
'''
def show_help():
    print ('usage:  python tomcat.py start|stop|show')
    print ('\n\n')
    print ('startup operation : ')
    print (start_operation)
    print ('----------------------------')
    print ('stop operation    : ')
    print (stop_operation)
    print ('----------------------------')
    print ('show operation    :')
    print (show_operation)
    print ('----------------------------')

if __name__=="__main__":
    operation = ''
    try:
        operation = sys.argv[1]
    except:
        show_help()
        sys.exit(0)
    if operation in start_operation:
        # start tomcat
        os.system('/app/tomcat1/bin/shutdown.sh')
        os.system('/app/tomcat1/bin/startup.sh')
        os.system('tail -f /app/tomcat1/logs/catalina.out')
    elif operation in stop_operation:
        # stop tomcat
        os.system('/app/tomcat1/bin/shutdown.sh')
        os.system('tail -f /app/tomcat1/logs/catalina.out')
    elif operation in show_operation:
        os.system('tail -f /app/tomcat1//logs/catalina.out')
    else:
        show_help()
        sys.exit(0)