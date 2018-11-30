# -*- coding: utf-8 -*-
# __author__ = 'Jasonleeyag'
from collections import namedtuple
User = namedtuple("User",["name","age","height","edu"])
user_tuple = ("jason",30,182)
user = User(*user_tuple,"master")
print(user.age,user.name,user.height)

#函数参数
def ask(*args,**kwargs):
    pass

