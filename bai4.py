# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 08:51:22 2024

@author: nguyenthuythaovy
"""

n=int(input("Nhập số nguyên dương N có 2 chữ số:"))
if 10<=n<=99:
    a=n//10
    b=n%10
    print("Tổng các chữ số của số nguyên dương N:",a+b)
else:
    print("Chỉ nhập số có 2 chữ số")
    