# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:55:10 2020

@author: naikk
"""

def computepay(h,r):
    if(h < 40):
       pay = float(h) * float(r)
       return pay
    else:
       pay = ((40*r) + ((h-40) * (r*1.5)))
       return pay
try: 
    hrs = input("enter hours:")
    rate = input ("enter rate:")
    h = float(hrs)
    r = float(rate)
    p = computepay(h,r)
    print("pay:", p)
except:
    print("Enter the hours and rate in numbers")
    