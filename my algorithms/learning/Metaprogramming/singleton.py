# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:39:55 2017

@author: junbai

Class Methods and Metamethods
"""

class Singleton(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance
    
class ASingleton(object):
    __metaclass__ = Singleton
    
a = ASingleton()
b = ASingleton()
assert a is b
print(a.__class__.__name__, b.__class__.__name__)

class BSingleton(object):
    __metaclass__ = Singleton
    
c = BSingleton()
d = BSingleton()
assert c is d
assert c is not a
