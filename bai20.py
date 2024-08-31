# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:13:03 2024

@author: nguyenthuythaovy  
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
max_number = a
if b > max_number:
    max_number = b
if c > max_number:
    max_number = c
print("Số lớn nhất là:", max_number)
