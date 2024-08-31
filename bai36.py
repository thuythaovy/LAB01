# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:24:56 2024

@author: nguyenthuythaovy 
"""

def sum_squares(n):
  return n * (n + 1) * (2*n + 1) // 6
n = int(input("Nhập số nguyên dương: "))
result = sum_squares(n)
print("Tổng là:", result)
