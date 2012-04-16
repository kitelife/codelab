#!/usr/bin/env python
# -*- coding:utf8 -*-
 
import functools
import datetime
import random
 

class timer(object):
    def __call__(self, method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            print 'start time: %s' % start
            method(*args, **kwargs)
            end = datetime.datetime.now()
            print 'end time: %s' % end
            #print 'using: %s' % (end - start).seconds
            print 'using: %s' % (end - start)
        return wrapper
 

def generator(length):
    return [random.randint(100000000, 100000000000) for i in range(length)]
 

class A(object):
    def __init__(self):
        self.a = generator(10000)
        self.b = generator(8000)
        self.diff = []
 
    @timer()
    def list_method(self):
        self.diff = [i for i in self.a if i not in self.b]
 
    @timer()
    def set_method(self):
        a = set(self.a)
        b = set(self.b)
        self.diff = list(a - (a & b))
    @timer()
    def sort_method(self):
        self.a.sort()
        self.b.sort()
        self.diff = [i for i in self.a if i not in self.b]
    @timer()
    def set_simpleMethod(self):
        a = set(self.a)
        b = set(self.b)
        self.diff = [i for i in a if i not in b]

if __name__ == "__main__":
    a = A()
    a.list_method()
    a.set_method()
    a.sort_method()
    a.set_simpleMethod()
