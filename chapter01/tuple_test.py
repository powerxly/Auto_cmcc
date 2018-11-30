# -*- coding: utf-8 -*-
# __author__ = 'Jasonleeyag'

name_tuple = ("jason","jason1")
user_tuple = ("jason",30,182,"beijing")
name,*other = user_tuple

print(name,other)

# class user:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

user = User(name='bobby',age=29)
