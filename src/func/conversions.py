# conversions flow:  any type  => Decimal  => any other type
from collections import deque

conversion = {
    'A': "10",
    'B': "11",
    'C': "12",
    'D': "13",
    'E': "14",
    'F': "15",
    
}

class conversions:
    @staticmethod
    def toDecimal(n:str,base:int):
        steps = []
        number = list(map(lambda x: conversion.get(x.upper(),x),list(n)))
        #...

#conversions.toDecimal("123ab123f",16)

