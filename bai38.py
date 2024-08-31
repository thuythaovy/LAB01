# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:30:15 2024

@author: nguyenthuythaovy 
"""

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
n = int(input("Nhập số nguyên dương: "))
result = factorial(n)
print("Tích giai thừa là:", result)
