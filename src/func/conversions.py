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
reverse_conversion = {v: k for k,v in conversion.items()}

class conversions:
    @staticmethod
    def toDecimal(n:str,base:int):
        if(n == "0"): return (0,[],[])
        steps = []
        rSteps = []
        n_reversed = n[::-1]
        numberList = list(map(lambda x: conversion.get(x.upper(),x),list(n_reversed)))
        for i in range(len(numberList)):
            r = int(numberList[i]) * (base**i)
            steps.append(f"{numberList[i]} * {base**i} = {r}")
            rSteps.append(r)

        return((sum(rSteps),steps,rSteps))

    @staticmethod
    def decimalTo(n:int, base: int):
        if(n == 0): return ("0",[],[])
        steps = []
        rSteps = deque()
        up = n
        while(up > 0):
            rInt = up // base
            rRem =  up % base
            steps.append(f"{up} / {base} = {rInt} remainder = {rRem}")
            rSteps.appendleft(str(rRem))
            up = rInt
        final_digits = list(map(lambda x: reverse_conversion.get(x, x), rSteps))
        return(("".join(final_digits),steps,final_digits))
        

