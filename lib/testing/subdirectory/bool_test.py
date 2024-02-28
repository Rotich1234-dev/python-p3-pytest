#!/usr/bin/env python3

from bool_functions import return_true

def return_true():
    return True

def test_return_true():
    '''in bool_functions, function "return_true" returns True.'''
    assert return_true() == True
