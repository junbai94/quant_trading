# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:42:13 2017

@author: junbai

Seperate test
"""

class MetaBase(type):
    def __new__(meta, name, bases, dct):
        print ("meta: %s, name: %s in Metabase __new__" % (meta, name))
        cls = super(MetaBase, meta).__new__(meta, name, bases, dct)
        return cls
    
    def donew(cls, *args, **kwargs):
        print ("class:%s in MetaBase donew method" % cls)
        _obj = cls.__new__(cls, *args, **kwargs)
        return _obj, args, kwargs
    
    def doinit(cls, _obj, *args, **kwargs):
        print ("class: %s, object: %s in Metabase doinit method" % (cls, _obj))
        _obj.__init__(*args, **kwargs)
        return _obj, args, kwargs
    
    def __call__(cls, *args, **kwargs):
        print ("class: %s in MetaBase __call__ method" % cls)
        _obj, args, kwargs = cls.donew(*args, **kwargs)
        _obj, args, kwargs = cls.doinit(*args, **kwargs)
        return _obj
    
class MetaParams(MetaBase):
    def __new__(meta, name, bases, dct):
        print ("meta: %s, name: %s in MetaParams __new__" % (meta, name))
        cls = super(MetaParams, meta).__new__(meta, name, bases, dct)
        print ("class: %s in MetaParams __new__" % cls)
        return cls
    
    def donew(cls, *args, **kwargs):
        print("class: %s in MetaParams donew" % cls)
        _obj, args, kwargs = super(MetaParams, cls).donew(*args, **kwargs)
        
class LineRoot(object):
    __metaclass__ = MetaParams

line = LineRoot()

