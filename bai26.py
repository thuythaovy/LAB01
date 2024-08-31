# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:52:36 2024

@author: nguyenthuythaovy 
"""

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
ket_qua = a, b, c
print("Các số sau khi sắp xếp:", ket_qua)

n = int(input("Nhập một số nguyên: "))
chu_so = [int(ch) for ch in str(n)]
chu_so.sort()
so_moi = int(''.join(map(str, chu_so)))
print("Số mới:", so_moi)
