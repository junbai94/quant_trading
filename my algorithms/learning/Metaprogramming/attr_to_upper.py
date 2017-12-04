# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:29:38 2017

@author: junbai

Metaclass that change every attributes to upper case
"""

def to_upper(name, bases, dct):
    new_attr = dict()
    
    for name, val in dct.items():
        if name.startswith('__'):
            new_attr[name] = val
        else:
            new_attr[name.upper()] = val
    return name, bases, new_attr

class Metabase(type):
    def __new__(meta, name, args, kwargs):
        print (meta)
        print (args)
        print (kwargs)
        name, args, kwargs = to_upper(name, args, kwargs)
        cls = super(Metabase, meta).__new__(meta, name, args, kwargs)
        return cls
    
    
class Foo():
    __metaclass__ = Metabase
    
    def bar(self):
        pass
    


