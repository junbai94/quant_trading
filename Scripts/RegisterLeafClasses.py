# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:36:56 2017

@author: Junbai
"""

class RegisterLeafClasses(type):
    def __init__(cls, name, bases, nmspcs):
        super(RegisterLeafClasses, cls).__init__(name, bases, nmspcs)
        if not hasattr(cls, 'registry'):
            cls.registry = set()
        cls.registry.add(cls)
        cls.registry -= set(bases)
        
    def __iter__(cls):
        return iter(cls.registry)
    
    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])
    
class Color(object):
    __metaclass__ = RegisterLeafClasses
    
class Blue(Color): pass
class Red(Color): pass
class Yellow(Color): pass
class Green(Color): pass
class CeruleanBlue(Blue): pass