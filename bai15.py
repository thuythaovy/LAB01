# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:44:23 2024

@author: nguyenthuythaovy 
"""

import math
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
x = ((a+b) / (math.pow(a, 1/3) + math.pow(b, 1/3)) - math.pow(a*b, 1/3)) / math.pow(math.pow(a, 1/3) - math.pow(b, 1/3), 2)
print("Kết quả của biểu thức là:", x)
