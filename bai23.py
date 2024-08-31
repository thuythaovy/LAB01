# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:34:52 2024

@author: 
"""

import math 
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép: x = {x}")
else:
    print("Phương trình vô nghiệm")
