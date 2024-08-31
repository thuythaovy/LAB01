# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:22:43 2024

@author: nguyenthuythaovy 
"""

a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
if a == 0:
    if b == 0:
        print ("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Phương trình có nghiệm duy nhất:",x)
