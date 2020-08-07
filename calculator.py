#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def addition(a, b):
    """ Addition of 2 numbers """
    return a + b

if __name__ == '__main__':
    a, b= (10, 20)
    print("{}+{}={}".format(a, b, addition(a, b)))
    print("Ready for your computations")