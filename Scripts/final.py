# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:39:16 2017

@author: Junbai

Final class. Prevent a class from being inherited
"""

class final(type):
    def __init__(cls, name, bases, nmspcs):
        super(final, cls).__init__(name, bases, nmspcs)
        for klass in bases:
            if isinstance(klass, final):
                raise TypeError(str(klass.__name__) + " is final")
                
class A(object): 
    pass


class B(A):
    __metaclass__ = final
    
print B.__bases__
print isinstance(B, final)

class C(B):
    pass